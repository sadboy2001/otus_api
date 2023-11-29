import pytest
import requests


def test_openbrewery_get_breweries():
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url)
    assert response.status_code == 200


def test_openbrewery_get_brewery_by_id():
    brewery_id = "5128df48-79fc-4f0f-8b52-d06be54d0cec"
    url = f"https://api.openbrewerydb.org/breweries/{brewery_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['id'] == brewery_id

def test_openbrewery_get_brewery_by_address_1():
    brewery_id = "9c5a66c8-cc13-416f-a5d9-0a769c87d318"
    url = f"https://api.openbrewerydb.org/breweries/{brewery_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()['street'] == "407 Radam Ln Ste F200"

@pytest.mark.parametrize("brewery_type", ["micro", "regional"])
def test_openbrewery_get_breweries_by_type(brewery_type):
    url = f"https://api.openbrewerydb.org/breweries?by_type={brewery_type}"
    response = requests.get(url)
    assert response.status_code == 200
    assert all(brewery['brewery_type'] == brewery_type for brewery in response.json())


@pytest.mark.parametrize("state", ["California", "Colorado"])
def test_openbrewery_get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    assert response.status_code == 200
    assert all(brewery['state'] == state for brewery in response.json())