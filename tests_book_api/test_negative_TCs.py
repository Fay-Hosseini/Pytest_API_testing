import requests
import pytest
BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

""" Invalid endpoint returns 404 """
def test_invali_endpoint_returns_404():
    response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/invalid")
    assert response.status_code == 404

""" Invalid method returns error """
def test_invalid_method_returns_error():
    response = requests.post(BASE_URL)      #POST without body
    assert response.status_code in [400,405,415]

""" Non-existing book ID returns 404 """
def test_non_existing_book_id_returns_404():
    response = requests.get(f"{BASE_URL}/99999")
    assert response.status_code == 404