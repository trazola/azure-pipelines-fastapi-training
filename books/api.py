from fastapi import APIRouter, HTTPException, status
from pydantic import UUID4

from books import schemas
from books.openapi import BOOK_NOT_FOUND

router = APIRouter(prefix="/books", tags=["books"])

BOOKS = {}


@router.post(path="", status_code=status.HTTP_201_CREATED)
def create_book_endpoint(
    payload: schemas.BookCreatePayload,
) -> schemas.BookCreated:
    new_book = schemas.BookCreated(
        title=payload.title,
        author=payload.author,
    )
    BOOKS[new_book.id] = new_book
    return new_book


@router.get(path="")
def list_books_endpoint() -> list[schemas.BookCreated]:
    return list(BOOKS.values())


@router.delete(path="", status_code=status.HTTP_204_NO_CONTENT)
def clear_all_books_endpoint() -> None:
    BOOKS.clear()


@router.get(path="/{book_id}", responses=BOOK_NOT_FOUND)
def retrieve_book_endpoint(book_id: UUID4) -> schemas.BookCreated:
    try:
        return BOOKS[book_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No book found with the provided ID: '{book_id}'.",
        ) from None
