import pandas


def load_data(path: str) -> pandas.DataFrame:
    data = pandas.read_csv(path)
    return data
