import pytest
import requests
import json

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

# Load test data once at import
with open("test_data.json", "r") as f:
    TEST_DATA = json.load(f)

@pytest.fixture(scope="session")
def session():
    """Reusable requests session for all tests."""
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s

@pytest.fixture
def books(session):
    """Fetch all books once per test that needs them."""
    response = session.get(BASE_URL)
    assert response.status_code == 200
    return response.json()

# ---------- Parametrized Test Using JSON ----------
@pytest.mark.parametrize("book_id", TEST_DATA["book_ids"])
def test_specific_book_details(session, book_id):
    response = session.get(f"{BASE_URL}/{book_id}")
    assert response.status_code == 200
    book = response.json()

    # Verify fields exist
    for field in ["id", "title", "description", "pageCount", "publishDate"]:
        assert field in book
    assert book["id"] == book_id
