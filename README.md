# FastAPI Book Management Application

This is a simple REST API built with FastAPI for managing books. 

It provides endpoints for creating, reading, and deleting books. 

It uses Pydantic for data validation and serialization.

## Project Structure

This project is organized as a Python package called `books` with the following files:

- `utils.py`: Contains utility functions.
- `schemas.py`: Defines Pydantic models for data validation and serialization.
- `openapi.py`: Contains OpenAPI response types and error models.
- `api.py`: Defines FastAPI routes.
- `main.py`: Entry point of the application, creating a FastAPI application and including the router from `api.py`.

## Installation and Usage

To use this project, you need Python 3.11 or higher.

1. Clone this repository.
2. Navigate to the repo directory.
3. Install poetry
4. Install project:
    ```bash
    poetry shell
    poetry install
    ```

5. Run the application:

    ```bash
    uvicorn main:app --app-dir books --reload
    ```

6. Open your browser and visit `http://127.0.0.1:8000/docs`.

## Endpoints

- `POST /books`: Create a new book.
- `GET /books`: List all books.
- `GET /books/{book_id}`: Retrieve a specific book by ID.
- `DELETE /books/{book_id}`: Delete book.

## Testing

This project also includes a suite of tests to verify the functionality of the API. To run the tests, use the following command:

```bash
poe test
```
