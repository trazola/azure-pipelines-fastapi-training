from fastapi import FastAPI
from fastapi.responses import HTMLResponse


def setup_keepalive(app: FastAPI) -> None:
    app.add_route(
        path="/keepalive/k8s",
        route=HTMLResponse(content="OK"),
        include_in_schema=False,
    )
