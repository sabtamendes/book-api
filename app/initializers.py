from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.config import tortoise_config
from app.main_route import route


def init(app: FastAPI):
    init_db(app)
    init_routes(app)

# 
def init_routes(app: FastAPI):
    api_prefix = "/api"
    app.include_router(route, prefix=f"{api_prefix}")


def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url=tortoise_config.db_url,
        modules=tortoise_config.modules,
        generate_schemas=tortoise_config.generate_schemas,
        add_exception_handlers=True,
    )
