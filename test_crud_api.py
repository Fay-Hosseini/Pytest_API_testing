from crud_api import API_crud

posts = API_crud()

def test_get_post():
    response = posts.get_posts(1)
    assert response.status_code == 200
    assert "title" in response.json()

def test_create_post():
    response = posts.create_posts("pytest post", "created with POM", 1)
    assert response.status_code == 201
    assert response.json()["title"] == "pytest post"

def test_delete_post():
    response = posts.delete_posts(1)
    assert response.status_code in [200, 204]