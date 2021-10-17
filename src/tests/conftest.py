import asyncio
from copy import copy
from urllib.parse import urlparse
from uuid import uuid4

import asyncpg
import pytest
from tortoise import Tortoise

from core import config, settings


async def init_test_db() -> str:
    """Init test db for Tortoise"""
    conn = await asyncpg.connect(dsn=settings.db_uri)

    db_name = f"test_{str(uuid4())}"
    await conn.execute(
        f'CREATE DATABASE "{db_name}"'
    )
    await conn.close()

    config_ = copy(config.TORTOISE_ORM)
    old_url = urlparse(config_['connections']['default'])
    new_db_url = (
        f"{old_url.scheme}://{old_url.username}:{old_url.password}"
        f"@{old_url.hostname}:{old_url.port or 5432}/{db_name}"
    )
    config_['connections']['default'] = new_db_url
    await Tortoise.init(config=config_)
    await Tortoise.generate_schemas(safe=False)

    return db_name


async def drop_database(db_name: str) -> None:
    """Close all connections and drop db"""
    await Tortoise.close_connections()
    conn = await asyncpg.connect(dsn=settings.db_uri)
    await conn.execute(
        f'DROP DATABASE "{db_name}"'
    )
    await conn.close()


@pytest.fixture(scope='session')
def loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
async def initialize_tests(loop):
    db_name = await init_test_db()
    yield
    await drop_database(db_name=db_name)
