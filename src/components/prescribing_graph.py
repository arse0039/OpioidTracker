from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output, Input
from src.components.prescribe_opioid_api import get_year_and_rate

def render(app: Dash) -> html.Div:
    @app.callback(
        Output('prescribing-graph', 'figure'),
        [Input("state-dropdown", "value"),
         Input("county-dropdown", "value")]
    )
    def update_state_county(state, county):
        raw_state_county_data = get_year_and_rate(state, county)
        years, rate = raw_state_county_data
        fig = px.line(
            x=years, y=rate,
            title="Opioid Prescribing Data By State and County", height=425,
            labels={'x': 'Year', 'y': 'Percentage Rate'}
        )
        return fig
    return html.Div(
        className="graph",
        children=dcc.Graph(id='prescribing-graph'),
    )

#test