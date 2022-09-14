import requests
from geocode import zip_geocode

CLINIC_API = "https://findtreatment.samhsa.gov/locator/listing"
METERS_PER_MILE = 1609.344

def find_clinics(zip: str, distance: float, num_results: int) -> list[dict]:
    """
    Returns clinic data for the nearest num_results clinics to the provided ZIP code
    found within the provided distance in miles.
    Parameters
    ----------
    zip : str
        ZIP code to search for clinics in
    distance : float or int
        the distance in miles around the ZIP code to search for clinics in
    num_results : int
        the number of clinics to return
    
    Returns
    -------
    list of dict
        list of clinic data for the clinics found
    """
    lat, long = zip_geocode(zip)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "sType": "SA",
        "pageSize": num_results,
        "page": "1",
        "sAddr": f"{lat}, {long}",
        "limitType": "2",
        "limitValue": METERS_PER_MILE * distance,
        "sort": "0"
    }

    resp = requests.post(CLINIC_API, headers=headers, data=data).json()
    return resp["rows"]

print(find_clinics("98031", 20, 5))