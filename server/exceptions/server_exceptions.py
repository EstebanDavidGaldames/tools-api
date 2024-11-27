from .base_http_exceptions import BaseHTTPException


class InternalServerError(BaseHTTPException):
    description= 'Error sin manejo implementado. Contacte al administrador (sysadmin).'
    status_code= 500

class NotImplemented(BaseHTTPException):
    description= 'Funcionalidad no implementada.'
    status_code= 501
