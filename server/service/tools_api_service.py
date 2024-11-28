from typing import List

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse


class ToolsService:

    def __init__(self):
        # HACER: Instanciar repositorio
        pass

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        # HACER:
        # 1- Recibir el objeto de tipo NewToolRequest, convertirlo en <dict> y pasarlo a capa de repositorio.
        # 2- Recibir del repositorio la respuesta (puede ser diccionario u objeto) convertirla en objeto de tipo ToolResponse y retornarlo.
        pass

    def get_list(self, limit: int, offset: int) -> List[ToolResponse]:
        # HACER:
        # 1- Recibir los parámetros limit y offset y pasarlos a la capa de repositorio.
        # 2- Recibir la lista de diccionarios u objetos y convertirlos a una lista de objetos de tipo ToolResponse y retornarla.
        pass

    def get_by_id(self, id: int) -> ToolResponse:
        # HACER:
        # 1- Recibir el id de los parámetros y pasarlo a la capa de repositorio.
        # 2- Recibir el diccionario u objeto del repositorio y convertirlo en objeto de tipo ToolResponse y retornarlo.
        pass

    def update(self, id: int, new_tool_data: ToolRequest) -> ToolResponse:
        # HACER:
        # 1- Recibir los parámetros, convertimos new_tool_data a diccionario y lo pasamos a la capa de repositorio.
        # 2- Recibimos el diccionario u objeto actualizado de la capa de repositorio, lo convertimos en objeto ToolResponse y lo retornamos.
        pass

    def delete(self, id: int) -> None:
        # HACER:
        # 1- Pasar el id a la capa de repositorio y retornar.
        pass
