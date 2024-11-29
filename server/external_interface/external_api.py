# PARA PRUEBA DE OBTENCIÓN DE DATOS MEDIANTE API EXTERNA
import logging

import requests

from server.configs import app_settings
# from server.schemas.tools_api_schemas import NewToolRequest, ToolRequest, ToolResponse --> Importar cuando se implemente


logger = logging.getLogger(__name__)

class ExternalToolsDataApi():
    def __init__(self):
        self.client = requests.Session()
        self.external_url = app_settings.EXTERNAL_API

    def create(self, new_tool): # new_tool: NewToolRequest -> Object required
        pass

    def get_list(self, limit: int, offset: int):
        url = self.external_url + '/external-resource'
        params = {
            'limit': limit,
            'offset': offset,
        }
        response = self.client.get(url, params=params)
        logger.info(f'[GET] {response.url} : {response.status_code}')
        return response.json()

    def get_by_id(self, id: int):
        pass

    def update(self, id: int, new_tool_data): # new_tool_data: ToolRequest -> Object required
        pass

    def delete(self, id: int):
        pass
