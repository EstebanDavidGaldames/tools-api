from typing import List

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse
from server.repository import ToolsRepository
from server.exceptions import NotFound


class ToolsService:
    
    def __init__(self):
        self.repo = ToolsRepository()

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        new_tool_dict = new_tool.model_dump()
        tool_dict = self.repo.create(new_tool_dict)
        return ToolResponse(**tool_dict)

    def get_list(self, limit: int, offset: int) -> List[ToolResponse]:
        tool_list = self.repo.get_list(limit, offset)
        return [ToolResponse(**tool) for tool in tool_list]

    def get_by_id(self, id: int) -> ToolResponse:
        tool = self.repo.get_by_id(id)
        if tool is None:
            raise NotFound(f'La herramienta con ID {id} no se encontró.')
        return ToolResponse(**tool)

    def update(self, id: int, new_tool_data: ToolRequest) -> ToolResponse:
        updated_tool = self.repo.update(
            id, new_tool_data.model_dump(exclude_none=True))
        if updated_tool is None:
            raise NotFound(f'La herramienta con ID {id} no se encontó para actualizarse.')
        return ToolResponse(**updated_tool)

    def delete(self, id: int) -> None:
        if not self.repo.delete(id):
            raise NotFound(f'La herramienta con ID {id} no se encontró para eliminarse.')
