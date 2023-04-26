from loguru import logger
from .base import BaseSettings
from .config import ENV, IS_TEST_ENV
from .config import db_hostname, db_name, db_password, db_port, db_user

DB_MODELS = ["app.models.book_model"]
TEST_DB_URL =  (f"postgres://"f"{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}")
DB_URL = (f"postgres://"f"{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}")
MIGRATION_MODELS = DB_MODELS
MIGRATION_MODELS.append("app.models.book_model")


TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": MIGRATION_MODELS,
            "default_connection": "default",
        },
    },
}


class TortoiseSettings(BaseSettings):
    db_url: str
    modules: dict
    generate_schemas: bool

    @classmethod
    def generate(cls):
        # se o valor da var de ambiente for test então o generate_schemas será true
        if IS_TEST_ENV:
            db_url = TEST_DB_URL
            generate_schemas = True
        else:
            db_url = DB_URL
            generate_schemas = False

        modules = {"models": DB_MODELS}
        logger.info(f"Define ORM settings to env: {ENV}")
        return TortoiseSettings(
            db_url=db_url, modules=modules, generate_schemas=generate_schemas
            )
