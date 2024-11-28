from typing import List

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse


class ToolsRepository:

    def create(self, new_tool: NewToolRequest) -> ToolResponse:
        pass

    def get_list(self, limit: int, offset: int) -> List[ToolResponse]:
        pass

    def get_by_id(self, id: int) -> ToolResponse:
        pass

    def update(self, id: int, new_tool_data: ToolRequest) -> ToolResponse:
        pass

    def delete(self, id: int) -> None:
        pass
