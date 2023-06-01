from typing import Any, TypeAlias

from fastapi import status
from pydantic import BaseModel

OpenAPIResponseType: TypeAlias = dict[int | str, dict[str, Any]]


class ErrorModel(BaseModel):
    detail: str


BOOK_NOT_FOUND: OpenAPIResponseType = {
    status.HTTP_404_NOT_FOUND: {
        "model": ErrorModel,
        "content": {
            "application/json": {
                "examples": {
                    status.HTTP_404_NOT_FOUND: {
                        "summary": "Book not found",
                        "value": {
                            "detail": "No book found with the provided ID:"
                            " '7c926000-613b-468e-a17d-a3fa1e3ef0e8'.",
                        },
                    },
                },
            },
        },
    },
}
