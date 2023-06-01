from fastapi import FastAPI

from books.api import router

app = FastAPI()
app.include_router(router=router)
