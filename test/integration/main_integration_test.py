from fastapi.testclient import TestClient
from app.controllers.book_router import router
from fastapi.exceptions import RequestValidationError
import pytest


@pytest.fixture
def client():
    with TestClient(router) as test_client:
        yield test_client


def test_read_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# def test_post_book_success_integration(client):
#      response = client.post(
#          "/book",
#          json={
#             "title": "The Great Gatsby",
#             "author": "F. Scott Fitzgerald",
#             "professor":"Dumbledore"
#          }
#     )

#      assert response.status_code == 201
#      assert response.json() == {"magiCode": "JKSUDD"}


# should return a error messge when the field is missing
def test_post_book_missing_fields(client):
     book_data = {
         "title": "The Great Gatsby",
         "author": "F. Scott Fitzgerald",
     }
     with pytest.raises(RequestValidationError):
        client.post("/book", json=book_data)


# should return a error message when the field is empty
def test_post_book_empty_field(client):
     book_data = {
         "title": "The Great Gatsby",
         "author": "F. Scott Fitzgerald",
         "professor":""
     }
     with pytest.raises(RequestValidationError):
        client.post("/book", json=book_data)


# should return a book when the id exists
@pytest.mark.asyncio
def test_get_book_by_id_success_integration(client):
    book_id = 33
    response = client.get(f"/api/book/{book_id}")
    assert response.status_code == 200
    assert response.json() == {
            "id": 33,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "professor": "Dumbledore",
            "magicCode": "WGOKJY",
            "createdAt": "2023-05-30T19:34:03.634212+00:00"
        }


# should return not found when the id doesnt exists
def test_get_book_by_id_notExists(client):
    book_id = "id"
    response = client.get(f"/api/book/{book_id}")
    assert response.status_code == 404
    assert "Not Found" in response.text

