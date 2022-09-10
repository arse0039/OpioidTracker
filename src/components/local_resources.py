from dash import Dash, html


def render(app: Dash) -> html.Div:
    return html.Div(
        className="local-resources",
        children=[
            html.P("Local resources using the fancy API")
        ]
    )
