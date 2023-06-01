import uuid

from fastapi.testclient import TestClient

from books import schemas


def test_book_and_200_http_status_should_be_returned_when_book_have_been_created(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreatePayload,
) -> None:
    response = test_client.post(
        url="/books",
        json=correct_book_payload.dict(),
    )
    created_book = response.json()
    retrieve_response = test_client.get(url=f"/books/{created_book['id']}")
    assert retrieve_response.status_code == 200
    assert retrieve_response.json() == created_book


def test_http_404_exception_should_be_thrown_when_book_does_not_exist(
    test_client: TestClient,
) -> None:
    incorrect_uuid4 = uuid.uuid4()
    response = test_client.get(url=f"/books/{incorrect_uuid4}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"No book found with the provided ID: '{incorrect_uuid4}'.",
    }
