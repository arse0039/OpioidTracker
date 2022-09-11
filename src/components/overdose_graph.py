from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output, Input
from src.components.fatal_od_api import fatal_data, year_average
from src.components.state_abbreviations import abbreviations
from src.components.nonfatal_parser import non_fatal_data


def render(app: Dash, nf_data) -> html.Div:
    @app.callback(
        Output('overdose-graph', 'figure'),
        Input("state-dropdown", "value")
    )
    def update_state_fatal(value):
        raw_state_data = fatal_data(value)
        years, deaths = year_average(raw_state_data)
        if max(deaths) == 0:
            fig = px.line(
                x=years, y=deaths,
                title=f"Opioid Overdose Data for {value}", height=425,
                labels={'x': 'Year', 'y': 'Deaths'}, range_y=[0, 10]
            )
        else:
            fig = px.line(
                x=years, y=deaths,
                title="Opioid Overdose Data By State", height=425,
                labels={'x': 'Year', 'y': 'Deaths'}
            )

        state_abbr = abbreviations[value]
        #test = non_fatal_data(nf_data, state_abbr)
        #fig.add_scatter(x=nf_years, y=nf_deaths)

        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(id='overdose-graph'),
    )
