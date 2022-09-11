import requests

state_data = requests.get(
    'https://api.census.gov/data/2010/dec/sf1?get=NAME&for=state:*').json()

states = [state[0] for state in state_data[1:]]
print(states)
