from threading import local
from dash import Dash, html
from . import state_dropdown, county_dropdown, general_resources, local_resources, death_graph, prescribing_graph


def main_layout(app: Dash, data1, data2, data3) -> html.Div:
    return html.Div(
        className="main-div",
        children=[
            # header
            html.Div(
                children=[
                    html.H1(app.title, className="title-header"),
                    html.P(
                        "Opioids are a class of drugs commonly used in the treatment of pain. According to the CDC, in 2019,\
                20.4% of adults were loving with chronic pain and 7.4% experienced pain significant enough to \
                    limit life or work activities. As a result, the prescribing of opioids in America has increased over the \
                       past 23 years and with that has come an increased risk for addiction and opioid-related overdoses."),
                    html.P("As prescribing rates and increased and new opioid-class drugs came on the market, the FDA began \
                taking note of the increase in overdoses and in 2013 issued a letter describing the issue as the 'opioid epidemic'."),
                    html.P("In 2020, 9.3 million people over the age of 12 misused prescription opioids within the prior year. \
                During the same year, 75% of all overdose related deaths involved opioids."),
                    html.Hr(), ],
            ),
            # dropdown
            html.Div(
                className="dropdown",
                children=[
                    state_dropdown.render(app),
                    county_dropdown.render(app)]
            ),
            # graphs
            html.Div(
                className="graphs",
                children=[
                    prescribing_graph.render(app),
                    death_graph.render(app),
                ]
            ),
            # local info
            local_resources.render(app),
            # general info
            general_resources.render(app),
            # references?
            html.Div(
                'references?',
                className="dropdown-div",
            ),
        ]
    )
