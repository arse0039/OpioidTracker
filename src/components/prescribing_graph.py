from dash import Dash, html, dcc
import plotly.express as px

fig = px.line(
    x=["2018", "2019", "2020"], y=[1, 3, 2],
    title="Opioid Overdose Data By State", height=425,
    labels={'x': 'Year', 'y': 'Deaths'}
)

fig.add_scatter(x=["2018", "2019", "2020"], y=[7, 2, 6])


def render(app: Dash) -> html.Div:
    return html.Div(
        className="graph",
        children=dcc.Graph(figure=fig),
    )
