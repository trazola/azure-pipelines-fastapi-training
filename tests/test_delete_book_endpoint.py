import uuid

from fastapi.testclient import TestClient

from books import schemas


def test_http_404_exception_should_be_thrown_when_book_does_not_exist(
    test_client: TestClient,
) -> None:
    incorrect_uuid4 = uuid.uuid4()
    response = test_client.delete(url=f"/books/{incorrect_uuid4}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"No book found with the provided ID: '{incorrect_uuid4}'.",
    }


def test_book_should_be_deleted_and_204_http_status_returned_when_book_exist(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreatePayload,
) -> None:
    create_response = test_client.post(
        url="/books",
        json=correct_book_payload.dict(),
    )
    assert create_response.status_code == 201
    new_book = create_response.json()
    delete_response = test_client.delete(url=f"/books/{new_book['id']}")
    assert delete_response.status_code == 204
