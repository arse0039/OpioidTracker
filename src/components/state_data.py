import requests
"""
    CENSUS_API = 'https://api.census.gov/data/2010/dec/sf1'
    COUNTY_API = 'https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*'
    STATE_API = 'https://api.census.gov/data/2010/dec/sf1?get=NAME&for=state:*'
"""

state_data = requests.get(
    "https://api.census.gov/data/2010/dec/sf1?get=NAME&for=state:*").json()

state_names = [state[0] for state in state_data[1:]]
state_ids = [ids[1] for ids in state_data[1:]]

# specific state: https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*&in=state:01


def county_finder(id):
    counties = f"https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*&in=state:{id}"
    county_data = requests.get(counties).json()
    county_names = [county[0] for county in county_data[1:]]
    real_names = []
    for name in county_names:
        name_list = name.split(" County")
        name_list = name_list[0].split(", ")
        real_names.append(name_list[0])
    real_names.sort()
    return real_names
