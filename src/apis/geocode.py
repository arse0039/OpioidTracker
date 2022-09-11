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
    
    resp = requests.get(GEOCODE_API, params=params).json()
    return (resp["latt"], resp["longt"])