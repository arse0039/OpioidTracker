import json
import requests

def get_year_and_rate(state:str, county:str) -> dict:
    """
    Will return a dictionary that contains the year and 1 year change in opioid prescription rate for the
    entered state and county using the CMS API.

    Parameters
    ----------
    state:str
        state name to search for opioid prescription rate in, must be spelled correctly
    county:str
        county name to search for opioid prescription rate in, my be spelled correctly

    Returns
    -------
    dict
        a dictionary containing the the year and the respective 1 year change in opioid prescription rate, if available
    """
    if " " in county:
        temp_list = list(county)
        for char in temp_list:
            if temp_list[char] == " ":
                temp_list[char] = "%20"
        county = "".join(temp_list)
    response_API = requests.get(f'https://data.cms.gov/data-api/v1/dataset/94d00f36-73ce-4520-9b3f-83cd3cded25c/data?filter[Prscrbr_Geo_Lvl]=County&filter[Prscrbr_Geo_Desc]={state}%3A{county}&filter[Breakout_Type]=Totals')
    data = response_API.text
    parse_json = json.loads(data)

    year_and_rate = {}
    
    for entry in reversed(parse_json):
        if entry["Opioid_Prscrbng_Rate_1Y_Chg"] != "":
            year_and_rate[(entry["Year"])] = float(entry["Opioid_Prscrbng_Rate_1Y_Chg"])
        else:
            # When there is no data on the 1 year change in opioid prescription rates, mark data as unavailable
            year_and_rate[(entry["Year"])] = 0
    years = year_and_rate.keys()
    rate = year_and_rate.values()
    if len(years) == 0 or len(rate) == 0:
        years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
        rate = [0 for i in range(len(years))]
    return (years, rate)


print(get_year_and_rate("Washington", "King"))


