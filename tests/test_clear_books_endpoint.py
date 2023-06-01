from fastapi.testclient import TestClient

from books import schemas


def test_all_books_should_be_removed_and_204_http_status_returned_when_books_exist(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreatePayload,
) -> None:
    test_client.post(
        url="/books",
        json=correct_book_payload.dict(),
    )
    response = test_client.get(url="/books")
    assert len(response.json()) == 1
    clear_response = test_client.delete(url="/books")
    assert clear_response.status_code == 204
    response = test_client.get(url="/books")
    assert len(response.json()) == 0
