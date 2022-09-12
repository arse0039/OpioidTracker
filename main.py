from dash import Dash
import dash_bootstrap_components as dbc
from src.components.layout import main_layout
from src.data_parsing.data_parser import load_data

FATAL_DATA_PATH = "./data/Drug_Overdose_Death_Counts.csv"
NONFATAL_DATA_PATH = "./data/Non-Fatal-Overdose-Data.csv"
PRESCRIBING_DATA = "./data/Medicare_opioid_prescribing_data.csv"


def main():
    app = Dash(__name__, external_stylesheets=[dbc.themes.LUX],
               meta_tags=[{'name': 'viewport',
                           'content': 'width=device-width, initial-scale=1.0'}])

    fatal_data = load_data(FATAL_DATA_PATH)
    non_fatal_data = load_data(NONFATAL_DATA_PATH)
    prescribe_data = load_data(PRESCRIBING_DATA)
    app.title = "Opioid Tracker Dashboard"
    app.layout = main_layout(app)
    app.run(debug=False)


#test

if __name__ == "__main__":
    main()
