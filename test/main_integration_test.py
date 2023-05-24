from fastapi.testclient import TestClient
from app.routes.book_router import router
from fastapi.exceptions import RequestValidationError
import pytest


@pytest.fixture
def client():
    return TestClient(router)


def test_read_health(client):
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Sabta"}


def test_post_book(client):
    id = 1
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    category = "A novel about the decadence of the Jazz Age"
    response = client.post(
        "/book",
        json={
            "id": id,
            "title": title,
            "author": author,
            "category": category
        }
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": id,
        "title": title,
        "author": author,
        "category": category
    }


def test_post_book_missing_fields(client):
    book_data = {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        # "category": "A novel about the decadence of the Jazz Age"
    }
    with pytest.raises(RequestValidationError):
        client.post("/book", json=book_data)
