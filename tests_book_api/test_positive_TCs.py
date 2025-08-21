import requests
import pytest

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

""" Status code should be 200 """
def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

""" Response should be an array """
def test_response_is_array():
    response = requests.get(BASE_URL)
    data = response.json()
    assert isinstance(data, list)

""" Array should not be empty """
def test_response_not_empty():
    response = requests.get(BASE_URL)
    data = response.json()
    assert len(data) > 0

""" Each book should have an 'id' and 'title' """
def test_each_book_has_id_title():
    response = requests.get(BASE_URL)
    data = response.json()
    for book in data:
        assert 'id' in book
        assert 'title' in book

""" First book should contain expected fields """
def test_book_object_structure():
    response = requests.get(BASE_URL)
    first_book = response.json()[0]
    expected_fields = ["id", "title", "description", "pageCount", "excerpt", "publishDate" ]
    for field in expected_fields:
        assert field in first_book
    assert first_book["id"]