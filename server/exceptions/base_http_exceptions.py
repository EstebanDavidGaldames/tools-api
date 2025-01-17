from fastapi import HTTPException


class BaseHTTPException(HTTPException):
    status_code: int
    description: str

    def __init__(self, message: str = 'Default error message.'):
        super().__init__(status_code= self.status_code, detail= message)

    @classmethod
    def as_dict(cls) -> dict:
        return {'description': cls.description}
