from fastapi import FastAPI

from api import health_check


def define_routes(app: FastAPI) -> None:
    app.include_router(router=health_check.router)
