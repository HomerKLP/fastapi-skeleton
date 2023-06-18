import sqlalchemy as sa
from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column as column


class BaseModel(DeclarativeBase):
    id = column(BigInteger, primary_key=True)

    @classmethod
    async def create(cls, session: AsyncSession, **values) -> None:
        query = sa.Insert(cls).values(**values)
        await session.execute(query)
