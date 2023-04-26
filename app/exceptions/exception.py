# app/exceptions/exception.py

class AppBaseException(Exception):
    def __init__(self, status_code: int, context: dict):
        self.status_code = status_code
        self.detail = {"code": status_code, **context}
