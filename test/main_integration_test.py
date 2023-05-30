from fastapi.testclient import TestClient
from app.routes.book_router import router
from fastapi.exceptions import RequestValidationError
import pytest


@pytest.fixture
def client():
    with TestClient(router) as test_client:
        yield test_client


# def test_read_health(client):
#     response = client.get("/health/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello Sabta"}


def test_post_book(client):
    
    response = client.post(
        "/book",
        json={
            
           "title": "The Great Gatsby",
           "author": "F. Scott Fitzgerald",
           "professor":"Dumbledore"
        }
    )

    assert response.status_code == 201
    assert response.json() == {
      "magiCode": "JKSUDD"
    }


def test_post_book_missing_fields(client):
    book_data = {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
    }
    with pytest.raises(RequestValidationError):
        client.post("/book", json=book_data)
