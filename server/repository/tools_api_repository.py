from typing import List

from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse
# from server.external_interface import external_data_client --> Use it for external data resource
#from server.database import db_connection -> Para trabajar la base de datos
#from server.database.models import ToolModel -> Para trabajar la base de datos


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
