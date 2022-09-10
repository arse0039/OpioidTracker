from dash import Dash
from src.components.layout import main_layout


def main():
    app = Dash()
    app.title = "Opioid Tracker Dashboard"
    app.layout = main_layout(app)
    app.run(debug=False)


if __name__ == "__main__":
    main()
