from dash import Dash, html, dcc


def render(app: Dash) -> html.Div:
    state_data = ["Alaska", " Oregon", "Test"]
    return html.Div(
        children=[
            html.Div(children="State", className="state-drop-header"),
            dcc.Dropdown(
                className="dropdown-bar",
                id="state-dropdown",
                options=[{"label": state, "value": state}
                         for state in state_data],
                placeholder="Select a state",
                multi=False,
            )]
    )
