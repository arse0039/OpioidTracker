from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output, Input
from src.components.fatal_od_api import fatal_data, year_average


def render(app: Dash, ) -> html.Div:
    @app.callback(
        Output('overdose-graph', 'figure'),
        Input("state-dropdown", "value")
    )
    def update_state(value):
        raw_state_data = fatal_data(value)
        years, deaths = year_average(raw_state_data)
        if max(deaths) == 0:
            fig = px.line(
                x=years, y=deaths,
                title="Opioid Overdose Data By State", height=425,
                labels={'x': 'Year', 'y': 'Deaths'}, range_y=[0, 10]
            )
        else:
            fig = px.line(
                x=years, y=deaths,
                title="Opioid Overdose Data By State", height=425,
                labels={'x': 'Year', 'y': 'Deaths'}
            )
        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(id='overdose-graph'),
    )
