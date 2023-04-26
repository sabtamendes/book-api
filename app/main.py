from loguru import logger
from app.config.config import ENV
from fastapi import FastAPI
from app.initializers import init
from app.middlewares import book_validator_middleware

app = FastAPI(logger=logger)

# a função register_interceptor é um middleware que é chamado antes da aplicação
# arquivo middleware.py
book_validator_middleware(app)

init(app)

logger.info(f"Service was initialized! (env: {ENV})")

