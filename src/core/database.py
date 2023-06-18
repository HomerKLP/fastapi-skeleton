from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from . import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=0,
)
autocommit_engine = engine.execution_options(isolation_level="AUTOCOMMIT")


Session = async_sessionmaker(engine, expire_on_commit=False)

# Use autocommit session to skip begin-commit queries to DB
# it's typically faster when you don't need transaction block
ACSession = async_sessionmaker(autocommit_engine, expire_on_commit=False)
