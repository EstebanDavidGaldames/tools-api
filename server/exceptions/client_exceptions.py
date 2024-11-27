from .base_http_exceptions import BaseHTTPException


class BadRequest(BaseHTTPException):
    description= 'Request no válido.'
    status_code= 400

class NotFound(BaseHTTPException):
    description= 'No se encontró lo solicitado.'
    status_code= 404
