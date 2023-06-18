import os
from typing import Any, Callable, Optional


class EnvResolver:
    """
    Simple class for resolving and casting variables from system environment
    Usage:
    >>> EnvResolver.get_env("MY_VAR", default=1, cast=int)
    >>> 1
    """

    @classmethod
    def get_env(cls, key: str, default: Any = None, cast: Optional[Callable] = None) -> Any:
        env = os.getenv(key=key, default=default)
        if cast is None or env is None:
            return env
        elif cast is bool and isinstance(env, str):
            mapping = {
                "True": True,
                "true": True,
                "1": True,
                "False": False,
                "false": False,
                "0": False,
            }
            value = env.lower()
            if value not in mapping:
                raise ValueError(f"Config '{key}' has value '{value}'. Not a valid bool.")
            return mapping[value]
        return cls._try_to_cast(env=env, key=key, cast=cast)

    @staticmethod
    def _try_to_cast(env: str, key: str, cast: Callable) -> Any:
        try:
            return cast(env)
        except (TypeError, ValueError):
            raise ValueError(f"Config '{key}' has value '{env}'. Not a valid {cast.__name__}.")


get_env = EnvResolver.get_env
