import pytest
import requests
import csv
import os

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s

@pytest.fixture(scope="session")
def book_ids_from_csv():
    ids = []
    file_path = os.path.join(os.path.dirname(__file__), "test_data.csv")
    if not os.path.exists(file_path):
        pytest.fail(f"Test data file not found: {file_path}")
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ids.append(int(row["book_id"]))
    return ids

# Parametrize test at runtime using the fixture
def test_specific_book_details(session, book_ids_from_csv):
    for book_id in book_ids_from_csv:
        response = session.get(f"{BASE_URL}/{book_id}")
        assert response.status_code == 200, f"Failed to fetch book ID {book_id}"
        book = response.json()
        for field in ["id", "title", "description", "pageCount", "publishDate"]:
            assert field in book, f"Missing field {field} in book ID {book_id}"
        assert book["id"] == book_id, f"Book ID mismatch: expected {book_id}, got {book['id']}"
