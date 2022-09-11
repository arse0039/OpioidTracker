from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output, Input


years = [2019, 2020, 2021]


APP_TOKEN = "9eSpPa9ptEvK84kA5ZzQyuP1e"


fig = px.line(
    x=years, y=[1, 3, 2],
    title="Opioid Overdose Data By State", height=425,
    labels={'x': 'Year', 'y': 'Deaths'}
)


def render(app: Dash, ) -> html.Div:
    @app.callback(
        Output('overdose-graph', 'figure'),
        Input("state-dropdown", "value")
    )
    def update_state(value):
        data_api = f"https://data.cdc.gov/resource/xkb8-kh2a.json?state={value}&indicator=Opioids%20(T40.0-T40.4,T40.6)$$app_token={APP_TOKEN}"
        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(figure=fig, id='overdose-graph'),
    )
