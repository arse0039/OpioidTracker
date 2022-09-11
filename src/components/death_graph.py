from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from . import county_dropdown




fig = px.line(
    x=["2018", "2019", "2020"], y=[1, 3, 2],
    labels={'x': 'Year', 'y': 'Deaths'},
    template='simple_white',
    )

fig.update_traces(line_color='#00695c')
fig.update_layout(title_text="Fatal Opioid Overdoses By State", title_x=0.5, title_font_color="#712177")

def render(app: Dash) -> html.Div:
    return html.Div(
        dbc.Card(
            dbc.CardBody([
                county_dropdown.render(app),
                html.Br(),
                dcc.Graph(
                    figure = fig,
                    id = 'overdose-graph',
                    config={
                        'displayModeBar': False
                    }
                   
                ),
            ])
        )
        
    )


