from gc import DEBUG_COLLECTABLE
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

def render(app: Dash) -> html.Div:
    return html.Div(dbc.CardGroup([
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Medication Alternatives", className="card-title text-center mb-4 mt-4"),
                    html.Ul([
                        html.Li("Acetaminophen"),
                        html.Li("NSAIDs"),
                        html.Li("Nerve pain medications"),
                        html.Li("Antidepressants"),
                        html.Li("Topical agents"),
                        html.Li("Interventional pain management"),
                        html.Li("Non-opioid anesthetsia")]
                    )
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Therapeutic Alternatives", className="card-title text-center mb-4 mt-4"),
                    html.Ul([
                        html.Li("Cold and heat"),
                        html.Li("Regular physical activity"),
                        html.Li("Acupuncture"),
                        html.Li("Massage therapy"),
                        html.Li("Occupational therapy"),
                        html.Li("Physical therapy"),
                        html.Li("Mental health therapy")

                    ])
                ]
            )
        ),

        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("National Resources", className="card-title text-center mb-4 mt-4"),
                    html.Ul([
                        html.Li(create_link("https://www.hhs.gov/opioids/")),
                        html.Li(create_link("https://scdhec.gov/opioid-epidemic")),
                        html.Li(create_link("https://www.cdc.gov/drugoverdose/featured-topics/treatment-recovery.html"))
                    ])
                ]
            )
        )
    ])
)

def create_link(url):
    return html.A(html.P(str(url)), href=url)
