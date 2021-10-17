from fastapi import FastAPI

from core import define_routes, on_startup, on_shutdown

app = FastAPI()

define_routes(app=app)


@app.on_event(event_type="startup")
async def startup() -> None:
    await on_startup()


@app.on_event(event_type="shutdown")
async def shutdown() -> None:
    await on_shutdown()
