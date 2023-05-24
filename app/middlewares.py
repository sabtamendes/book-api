# # app/middlewares.py

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from app.schemas.book_schema import BookSchema
# from app.exceptions.exception import AppBaseException
# from app.exceptions.base import BookValidationException


# def book_validator_middleware(app: FastAPI):
#     @app.middleware("http")
#     async def validate_book(request: Request, call_next):
#         if request.method == "POST" or request.method == "PUT":
#             try:
#                 data = await request.json()
#                 print(data, "data middleware")
#                 book = BookSchema(**data)
#                 request.state.book = book
#             except AppBaseException as exc:
#                 return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)
#         response = await call_next(request)
#         return response
