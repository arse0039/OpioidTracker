from dash import Dash, html
import dash_bootstrap_components as dbc
from . import overdose_graph, app_title, state_dropdown, alternatives, county_dropdown, general_resources, local_resources, prescribing_graph

def main_layout(app: Dash, non_fatal_data) -> html.Div:
    return html.Div(dbc.Container(
        className="main-div",
        children=[
            # header
            html.Div(
                app_title.render(app)
            ),
            # dropdown
            dbc.Row(children=[
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(state_dropdown.render(app))),
                        width=6),
                    dbc.Col(
                        dbc.Card(
                        dbc.CardBody(county_dropdown.render(app))),
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
                            dbc.CardBody(overdose_graph.render(app, non_fatal_data))),
                        width=6),
                    
            ], className="g-0"),
            html.Div(
                alternatives.render(app),
            ),
        ]
    )
)