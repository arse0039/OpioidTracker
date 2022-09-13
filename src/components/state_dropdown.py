from dash import Dash, html, dcc
from src.components.state_data import state_names


def render(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.Div(children="State", className="state-drop-header"),
            dcc.Dropdown(
                className="dropdown-bar",
                id="state-dropdown",
                options=[{"label": state, "value": state}
                         for state in state_names],
                value="Alabama",
                multi=False,
            )]
    )