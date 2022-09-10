from dash import Dash, html, dcc


def render(app: Dash) -> html.Div:
    county_data = ["county1", "county2", "county3"]
    return html.Div(
        children=[
            html.Div(children="County", className="county-drop-header"),
            dcc.Dropdown(
                className="dropdown-bar",
                id="county-dropdown",
                options=[{"label": county, "value": county}
                         for county in county_data],
                placeholder="Select a county",
                multi=False,
            )]
    )
