from tortoise import Tortoise

from core.config import TORTOISE_ORM


async def init_db() -> None:
    await Tortoise.init(config=TORTOISE_ORM)


async def on_startup() -> None:
    await init_db()
