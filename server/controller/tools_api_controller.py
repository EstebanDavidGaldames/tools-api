from typing import List

# from fastapi import HTTPException # No se utiliza - Eliminar import

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse
from server.exceptions import BaseHTTPException, InternalServerError, NotFound
from server.service import ToolsService


class ToolsController:
    def __init__(self):
        self.service = ToolsService()

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        try:
            # Llamada a la capa de servicio para que realice la acción correspondiente
            # Retorna data de ejemplo
            #return ToolResponse(id= 1, **new_tool.model_dump())
            return self.service.create(new_tool)
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
            #return []
            return self.service.get_list(limit, offset)
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
            #return NotFound(f'No se encontró la herramienta con id = {id}.')
            return self.service.get_by_id(id)
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
            #return ToolResponse(id=id, **new_tool_data.model_dump())
            return self.service.update(id, new_tool_data)
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
            #return
            self.service.delete(id)
        except BaseHTTPException as ex:
            # Se debe implementar loggin
            raise ex
        except Exception:
            # Error no implementado en ToolsController.create
            raise InternalServerError()
