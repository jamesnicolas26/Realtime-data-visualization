import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import asyncio
import websockets

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-update-graph', style={"height": "60vh"}),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # 1 second
        n_intervals=0
    )
])

@app.callback(
    dash.dependencies.Output('live-update-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Example: Simulate data
    df = px.data.gapminder().query("year==2007")
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     hover_name="country", log_x=True, size_max=60)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
