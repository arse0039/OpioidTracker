from dash import Dash, html, dcc
import plotly.express as px

years = ["2018", "2019", "2020"]
test_values1 = [5, 1, 2]
test_values2 = [2, 3, 7]

max_val = max(test_values1, test_values2)

fig = px.line(
    x=["2018", "2019", "2020"], y=test_values1,
    title="Opioid Overdose Data By State", height=425,
    labels={'x': 'Year', 'y': 'Deaths'}, range_y=[0, max_val]
)

fig.add_scatter(x=["2018", "2019", "2020"], y=test_values2)


def render(app: Dash) -> html.Div:
    return html.Div(
        className="graph",
        children=dcc.Graph(figure=fig),
    )
