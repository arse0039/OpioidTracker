from dash import Dash, html


def render(app: Dash) -> html.Div:
    return html.Div(
        className="general-resources",
        children=[
            html.P("Drug Alternatives: Acetaminophen, NSAIDs, Gabapentin/pregabalin, Tricyclic antidepresents and serotonin/norephinephrine reuptake inhibitors, Topical Agents - Lidocaine, capsaicin, NSAIDs")
        ]
    )
