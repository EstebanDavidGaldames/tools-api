import logging
from typing import List

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse
from server.exceptions import BaseHTTPException, InternalServerError
from server.service import ToolsService


logger = logging.getLogger(__name__)


class ToolsController:
    def __init__(self):
        self.service = ToolsService()

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        try:
            logger.debug(f'Ingreso de nueva herramienta: {new_tool.tool_name}.')
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna data de ejemplo
            #return ToolResponse(id= 1, **new_tool.model_dump())
            return self.service.create(new_tool)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en el controlador {__name__}.create')
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[ToolResponse]:
        try:
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en el controlador {__name__}.get_list')
            raise InternalServerError()

    def get_by_id(self, id: int) -> ToolResponse:
        try:
            logger.debug(f'Consulta de herramienta - ID: {id}.')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en el controlador {__name__}.get_by_id')
            raise InternalServerError()
    
    def update(self, id: int, new_tool_data: ToolRequest) -> ToolResponse:
        try:
            return self.service.update(id, new_tool_data)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en el controlador {__name__}.update')
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(f'Error no contemplado en el controlador {__name__}.delete')
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor - STATUS CODE {ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error en la solicitud - STATUS CODE {ex.status_code} : {ex.description}')
        raise ex
