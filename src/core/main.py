from logging import config as logging_config

from fastapi import FastAPI

from api import health_check
from core import settings

app = FastAPI()

# define routes
app.include_router(router=health_check.router)

# initialize logging config
logging_config.dictConfig(settings.LOGGING)


@app.on_event(event_type="startup")
async def startup() -> None:
    pass


@app.on_event(event_type="shutdown")
async def shutdown() -> None:
    pass
