import pandas as pd


test = {
    'Year': [2018, 2019, 2020],
    'Non-Fatal': [5, 1, 2],
    'Fatal': [2, 3, 7]
}


df1 = pd.DataFrame(test)


print(df1)
