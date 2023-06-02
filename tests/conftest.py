import pytest
from fastapi.testclient import TestClient

from books import schemas
from books.api import BOOKS
from books.main import app


@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app=app)


@pytest.fixture()
def correct_book_payload() -> schemas.BookCreatePayload:
    return schemas.BookCreatePayload(
        author="John Doe",
        title="Software Engineer",
    )


@pytest.fixture(autouse=True)
def _clear_books() -> None:
    BOOKS.clear()
