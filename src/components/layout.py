from dash import Dash, html
import dash_bootstrap_components as dbc
from . import overdose_graph, state_dropdown, county_dropdown, general_resources, local_resources, prescribing_graph, app_title, alternatives


def main_layout(app: Dash) -> html.Div:
    return html.Div(
        className="main-div",
        children=[
            # header
            html.Div(
                app_title.render(app)
            ),
            # dropdown
            dbc.Row(children=[
                    dbc.Col(
                        state_dropdown.render(app),
                        width=6),
                    dbc.Col(
                        county_dropdown.render(app),
                        width=6),
            ], className="g-0"),
            # graphs
            dbc.Row(children=[
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(prescribing_graph.render(app))),
                        width=6),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(overdose_graph.render(app))),
                        width=6),
                    
            ], className="g-0"),
            html.Div(
                alternatives.render(app),
            ),
        ]
    )
