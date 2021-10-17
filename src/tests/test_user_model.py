import pytest

from models import User


@pytest.mark.asyncio
async def test_create_user() -> None:
    data = {
        "username": "username",
        "first_name": "first_name",
        "last_name": "last_name",
        "password_hash": "password_hash",
    }
    user = await User.create(**data)
    assert user
    assert str(user) == "username"
