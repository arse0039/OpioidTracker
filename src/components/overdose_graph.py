from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Output, Input
from src.components.fatal_od_api import fatal_data, year_average
from src.components.state_abbreviations import abbreviations
from src.components.nonfatal_parser import non_fatal_data
import plotly.graph_objects as go



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


        fig = px.line(
            template='simple_white',
        )

        fig.update_xaxes(tickangle=45, title="Year")
        fig.update_yaxes(title='% Change in Overdose Events')
        fig.update_traces(line_color='#527c88')
        fig.update_layout(title=f"Opioid Overdoses in {value}", title_x=0.5, title_font_color="#10217d")
        fig.add_scatter(x=nf_year, y=nf_od, name="Non-Fatal", line_color='#527c88')
        fig.add_scatter(x=years, y=deaths, name="Fatal", line_color='#10217d')
        return fig

    return html.Div(
        className="graph",
        children=dcc.Graph(id='overdose-graph', config={'displayModeBar':False}),
    )