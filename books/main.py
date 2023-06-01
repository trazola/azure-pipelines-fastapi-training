from fastapi import FastAPI

from books.api import router
from books.keepalive import setup_keepalive

app = FastAPI()
app.include_router(router=router)
setup_keepalive(app=app)
