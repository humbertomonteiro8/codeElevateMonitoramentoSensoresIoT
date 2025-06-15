import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import psycopg2
from data_consumer.consumer_settings import DB_SETTINGS


def fetch_sensor_data():
    conn = psycopg2.connect(**DB_SETTINGS)
    query = """
        SELECT timestamp, pressure
        FROM sensor_data
        LIMIT 2000
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def aggregate_pressure_by_year(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["year"] = df["timestamp"].dt.year
    agg = df.groupby("year")["pressure"].mean().reset_index()
    agg.columns = ["Ano", "Pressão Média"]
    return agg


app = dash.Dash(__name__)
app.title = "Dashboard - Evolução da Pressão"

app.layout = html.Div([
    html.H2("📊 Evolução Anual da Pressão"),
    html.P(
        "Gráfico de linha com a média anual da pressão dos sensores. "
        "Ideal para visualizar tendências e detectar anomalias."
    ),
    dcc.Interval(id='interval', interval=60 * 1000, n_intervals=0),
    dcc.Graph(id='pressure-line-graph')
])


@app.callback(
    Output('pressure-line-graph', 'figure'),
    Input('interval', 'n_intervals')
)
def update_graph(n):
    df = fetch_sensor_data()
    df_yearly = aggregate_pressure_by_year(df)
    fig = px.line(
        df_yearly,
        x="Ano",
        y="Pressão Média",
        markers=True,
        title="Média Anual da Pressão dos Sensores"
    )
    fig.update_layout(xaxis_title="Ano", yaxis_title="Pressão Média")
    return fig


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
