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
            labels={'x': 'Year', 'y': 'Percentage Rate'},
            template='simple_white'
        )
        fig.update_xaxes(tickangle=45)
        fig.update_traces(line_color='#527c88')
        fig.update_layout(title_text=f"Opioid Prescriptions in {county}, {state}", title_x=0.5, title_font_color="#10217d")
        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(id='prescribing-graph',
                            config={'displayModeBar':False}),
    )

#test