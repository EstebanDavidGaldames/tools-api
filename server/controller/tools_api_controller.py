from typing import List

from fastapi import HTTPException

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse
from server.exceptions import BaseHTTPException, InternalServerError, NotFound


class ToolsController:
    def __init__(self):
        pass #Refiere a capa de servicio

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna data de ejemplo
            return ToolResponse(id= 1, **new_tool.model_dump())
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()

    def get_list(self, limit: int, offset: int) -> List[ToolResponse]:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna data de ejemplo
            return []
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()

    def get_by_id(self, id: int) -> ToolResponse:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna ejemplo de error
            return NotFound(f'No se encontró la herramienta con id = {id}.')
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()
    
    def update(self, id: int, new_tool_data: ToolRequest) -> ToolResponse:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna ejemplo
            return ToolResponse(id=id, **new_tool_data.model_dump())
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna None
            return
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()
