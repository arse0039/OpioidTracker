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
        state_abbr = abbreviations[value]
        nf_year, nf_od = non_fatal_data(nf_data, state_abbr)
        # if max(deaths) == 0:
        #     fig = px.line(
        #         x=years, y=deaths,
        #         title=f"Opioid Overdose Data for {value}", height=425,
        #         labels={'x': 'Year', 'y': 'Deaths'}, range_y=[0, 10]
        #     )
        # else:
        fig = px.line(
            x=years, y=deaths,
            title=f"Opioid Overdose Data By {value}", height=425,
            labels={'x': 'Year', 'y': '% Change in Overdose Events'}
        )

        fig.update_layout(legend_title="Overdose Type")
        # fig.update_traces(name="Fatal")

        fig.add_scatter(x=nf_year, y=nf_od, name="Non-Fatal")

        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(id='overdose-graph'),
    )
