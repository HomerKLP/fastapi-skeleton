from fastapi import FastAPI

from core import define_routes, on_startup

app = FastAPI()

define_routes(app=app)


@app.on_event(event_type="startup")
async def startup() -> None:
    await on_startup()
