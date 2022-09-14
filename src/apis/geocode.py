import requests

GEOCODE_API = "https://geocode.xyz/"

def zip_geocode(zip: str) -> tuple[str, str]:
    """
    Returns the latitude and longitude of the provided ZIP code.
    Parameters
    ----------
    zip : str
        ZIP code to find latitude and longitude for
    
    Returns
    -------
    tuple of str
        the latitude and longitude of the ZIP code
    """
    params = {
        "locate": zip,
        "region": "US",
        "json": "1"
    }
    try:
        resp = requests.get(GEOCODE_API, params=params).json()
    except requests.exceptions.RequestException:
        raise ValueError("Invalid response received")

    if "error" in resp or "latt" not in resp or "longt" not in resp:
        raise ValueError("No valid result found")
    
    return (resp["latt"], resp["longt"])

def city_state_geocode(city: str, state: str) -> tuple[str, str]:
    """
    Returns the latitude and longitude of the provided city and state.
    Parameters
    ----------
    city : str
        city to find latitude and longitude for
    state : str
        state to find latitude and longitude for
    
    Returns
    -------
    tuple of str
        the latitude and longitude of the city and state
    """
    params = {
        "locate": f"{city}, {state}",
        "region": "US",
        "json": "1"
    }
    try:
        resp = requests.get(GEOCODE_API, params=params).json()
    except requests.exceptions.RequestException:
        raise ValueError("Invalid response received")
    
    if "error" in resp or "latt" not in resp or "longt" not in resp:
        raise ValueError("No valid result found")
    
    return (resp["latt"], resp["longt"])