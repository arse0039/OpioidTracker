from dash import Dash, html
import dash_bootstrap_components as dbc

def render(app: Dash) -> html.Div:
    return html.Div(
    dbc.Card(
        dbc.CardBody(
            [html.H1(app.title, className='text-center mb-4 mt-4'),
            html.P("© Rebecca Chen, Cristina Rosace, Blake Hakkila, Brandon Arsenault", className='text-center'),
            html.P("Opioids are a class of drugs commonly used in the treatment of pain. According to the CDC, in 2019, 20.4% of adults were living with chronic pain and 7.4% experienced pain significant enough to limit life or work activities. As a result, the opioid prescriptions in America has increased over the past 23 years. As risk for opioid addiction and opioid related overdoses have escalated, we are now experiencing an opioid crisis. ", className='text-center')]
            ))
    )   
