from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from src.components.state_data import state_names, state_ids, county_finder


def render(app: Dash) -> html.Div:
    @app.callback(
        Output("county-dropdown", "options"),
        Input("state-dropdown", "value")
    )
    def get_county(value):
        index = state_names.index(value)
        actual_id = state_ids[index]
        county_list = county_finder(actual_id)
        return [{"label": county, "value": county}
                for county in county_list]

    return html.Div(
        children=[
            html.Div(children="County", className="county-drop-header"),
            dcc.Dropdown(
                className="dropdown-bar",
                id="county-dropdown",
                value="Autauga",
                multi=False,
            )]
    )
