from fastapi.testclient import TestClient
from freezegun import freeze_time

from books import schemas


def test_empty_list_and_200_http_status_should_be_returned_when_no_books_have_been_created(
    test_client: TestClient,
) -> None:
    response = test_client.get(url="/books")
    assert response.status_code == 200
    assert response.json() == []


@freeze_time(time_to_freeze="2012-01-14 12:00:01")
def test_books_and_200_http_status_should_be_returned_when_books_have_been_created(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreated,
) -> None:
    create_response = test_client.post(url="/books", json=correct_book_payload.dict())
    assert create_response.status_code == 201
    response = test_client.get(url="/books")
    created_books = response.json()
    assert response.status_code == 200
    assert created_books == [create_response.json()]
    test_client.delete(url="/books")
