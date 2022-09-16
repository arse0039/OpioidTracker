import pandas
from statistics import mean


PATH = "./data/Non-Fatal-Overdose-Data.csv"

data = pandas.read_csv(PATH, skiprows=3)


def non_fatal_data(data, state):
    year = [2018, 2019, 2020, 2021, 2022]
    yearly_data = {}
    for ele in year:
        data_string = f"8Year2YearSameMonth{state}"
        mask = (
            (data["state"] == state) & (data["comparisonType"]
                                        == data_string) & (data["startYear"] == ele)
        )
        filtered_data = data.loc[mask, :]
        list_values = filtered_data["opioidPercentageChange"].to_list()
        filtered = list(
            filter(lambda value: value != 'suppressed' and value != 'missing', list_values))
        filtered_to_int = [float(val) for val in filtered]
        if len(filtered_to_int) > 0:
            average_filtered = round(mean(filtered_to_int), 2)
        else:
            average_filtered = 0
        yearly_data[str(ele)] = average_filtered

    year = list(sorted(yearly_data.keys()))
    deaths = list(yearly_data.values())
    return (year, deaths)
