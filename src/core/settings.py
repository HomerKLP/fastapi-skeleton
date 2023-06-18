import logging
from os import path, pardir

from core.env_resolver import get_env

# Core
DEBUG = get_env("DEBUG", default=False, cast=bool)
CORE_DIR = path.dirname(__file__)
WORK_DIR = path.abspath(path.join(CORE_DIR, pardir))
PARENT_DIR = path.abspath(path.join(WORK_DIR, pardir))

# Database
DATABASE_POOL_SIZE = get_env("DB_POOL_SIZE", default=10, cast=int)
DATABASE_HOST = get_env("DB_HOST")
DATABASE_PORT = get_env("DB_PORT", cast=int)
DATABASE_NAME = get_env("DB_NAME")
DATABASE_USER = get_env("DB_USER")
DATABASE_PASSWORD = get_env("DB_PASSWORD")
DATABASE_URL = (
    f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# Logging
LOG_DIR = path.join(PARENT_DIR, "logs")
LOG_DIR_EXISTS = path.isdir(LOG_DIR)
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.ERROR
LOG_FILE_SIZE_BYTES = get_env("APP_SETTINGS_LOG_FILE_SIZE_GB", default=1, cast=int) * 1024**3
LOG_FILES_COUNT = get_env("APP_SETTINGS_LOG_FILES_COUNT", default=2, cast=int)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "logging.Formatter",
            "format": "%(levelname)s [%(asctime)s] [%(name)s] %(filename)s:%(lineno)s %(message)s",
            "datefmt": "%d/%b/%Y:%H:%M:%S %z",
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "datefmt": "%d/%b/%Y:%H:%M:%S %z",
            "fmt": "%(levelname)s [%(asctime)s] [%(name)s] %(pathname)s %(lineno)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": LOGGING_LEVEL,
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "file_handler": {
            "level": LOGGING_LEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "filename": path.join(LOG_DIR, "debug.log"),
            "maxBytes": LOG_FILE_SIZE_BYTES,
            "backupCount": LOG_FILES_COUNT,
        },
    },
    "root": {
        "level": LOGGING_LEVEL,
        "handlers": ["console", "file_handler"] if LOG_DIR_EXISTS else ["console"],
    },
}