from typing import Any

import pytest
from fastapi.testclient import TestClient
from freezegun import freeze_time

from books import schemas


@freeze_time(time_to_freeze="2012-01-14 12:00:01")
def test_book_should_be_created_and_201_http_status_returned_when_payload_is_correct(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreatePayload,
) -> None:
    response = test_client.post(
        url="/books",
        json=correct_book_payload.dict(),
    )
    assert response.status_code == 201
    book = response.json()
    assert book["title"] == correct_book_payload.title
    assert book["author"] == correct_book_payload.author
    assert book["created_at"] == "2012-01-14T12:00:01+00:00"
    test_client.delete(url="/books")


@pytest.mark.parametrize(
    ("field_name", "field_value"),
    [
        ("title", None),
        ("author", None),
    ],
)
def test_http_422_exception_should_be_thrown_when_invalid_payload_schema_is_provided(
    test_client: TestClient,
    correct_book_payload: schemas.BookCreatePayload,
    field_name: str,
    field_value: Any,
) -> None:
    payload_as_dict = correct_book_payload.dict()
    payload_as_dict[field_name] = field_value
    response = test_client.post(url="/books", json=payload_as_dict)
    assert response.status_code == 422
