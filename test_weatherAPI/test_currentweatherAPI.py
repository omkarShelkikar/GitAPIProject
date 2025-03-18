import requests

from helper.readenv import getAPIkey,getBaseUrl


def make_request(params):
    base_url = getBaseUrl()
    response = requests.get(f"{base_url}/current?", params=params)

    # Check if the status code is OK (200)
    check_status_code(response)

    return response.json()

def check_status_code(response):
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def validate_response(json_data, expected_key="temperature"):
    # Validate if the expected key is present in the response data
    assert expected_key in json_data["current"], f"Expected '{expected_key}' in response"

def test_current_location_weather_with_valid_api_key():
    api_key = getAPIkey()
    params = {
        "access_key": api_key,
        "query": "New Delhi"
    }
    json_data = make_request(params)
    validate_response(json_data)

def test_current_location_weather_with_invalid_api_key():
    invalid_api_key = "e48e42155209bacd062a4f7c0b654690"
    params = {
        "access_key": invalid_api_key,
        "query": "New Delhi"
    }
    json_data = make_request(params)
    assert "error" in json_data, "Expected an error in the response"
    assert json_data["error"]["info"] == "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]"