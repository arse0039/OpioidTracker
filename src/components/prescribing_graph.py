from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from . import state_dropdown



fig = px.line(
    x=["2018", "2019", "2020"], y=[1, 3, 2],
    labels={"x": "Year", "y": "Opioid Pescribing Rate"},
    template='simple_white'
)

fig.update_traces(line_color='#304c94')
fig.update_layout(title_text="Opioid Prescription by State and County", title_x=0.5, title_font_color="#712177")


def render(app: Dash) -> html.Div:
    return html.Div(
        dbc.Card(
            dbc.CardBody([
                state_dropdown.render(app),
                html.Br(),
                dcc.Graph(
                    figure=fig,
                    id = 'death-graph',
                    config={
                        'displayModeBar': False
                    }
                )
            ])

        )

        
        
    )

#test