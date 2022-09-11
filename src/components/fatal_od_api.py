import requests
from statistics import mean

APP_TOKEN = "9eSpPa9ptEvK84kA5ZzQyuP1e"
# https://data.cdc.gov/resource/xkb8-kh2a.json?state_name=Kansas&indicator=Opioids%20(T40.0-T40.4,T40.6)$$app_token=9eSpPa9ptEvK84kA5ZzQyuP1e


def fatal_data(value: str) -> dict:
    data_api = f"https://data.cdc.gov/resource/xkb8-kh2a.json?state_name={value}&indicator=Opioids%20(T40.0-T40.4,T40.6)"
    state_fatal = requests.get(data_api).json()
    graph_data = {}
    for key in state_fatal:
        if "data_value" in key:
            if key["year"] not in graph_data:
                graph_data[key["year"]] = [int(key["data_value"])]
            else:
                graph_data[key["year"]].append(int(key["data_value"]))
    return graph_data


def year_average(graph_data: dict) -> tuple:
    """
    Extracts the years and averaged death data for use in graphing of
    the data based on the state.
    """
    for item in graph_data.keys():
        value = graph_data[item]
        value = int(mean(value))
        graph_data[item] = value
    years = list(graph_data.keys())
    deaths = list(graph_data.values())
    death_percent_change = [0]
    for i in range(1, len(deaths)):
        change = ((deaths[i] - deaths[i-1])/deaths[i-1])*100
        death_percent_change.append(round(change, 2))
    if len(years) == 0:
        years = ['2015', '2016', '2017', '2018',
                 '2019', '2020', '2021', '2022']
        death_percent_change = [0 for i in range(len(years))]
    return (years, death_percent_change)


test = fatal_data("Alabama")
print(year_average(test))
