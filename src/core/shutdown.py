from tortoise import Tortoise


async def on_shutdown() -> None:
    await Tortoise.close_connections()
