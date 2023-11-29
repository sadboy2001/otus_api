import pytest
import requests

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL to test")
    parser.addoption("--status_code", action="store", default=200, help="Expected status code")

def test_url_status(pytestconfig):
    url = pytestconfig.getoption("url")
    status_code = pytestconfig.getoption("status_code")
    response = requests.get(url)
    assert response.status_code == status_code
