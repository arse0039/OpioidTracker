from threading import local
from dash import Dash, html
import dash_bootstrap_components as dbc
from . import state_dropdown, county_dropdown, general_resources, local_resources, death_graph, prescribing_graph, app_title


def main_layout(app: Dash, data1, data2, data3) -> html.Div:
    drop_downs = [
        dbc.Col(state_dropdown.render(app), width=4),
        dbc.Col(county_dropdown.render(app), width=4)
    ]
    return html.Div(dbc.Container([
            html.Br(),
            dbc.Row(
                   dbc.Col(
                       app_title.render(app),
                       width=12
                   )
            ),

            dbc.Row ([
                    dbc.Col (
                        prescribing_graph.render(app),
                        width=6),
        
                    dbc.Col(
                        death_graph.render(app),
                        width=6)
                    
            ], className="g-0"),

  # test

        ]))
        
       

