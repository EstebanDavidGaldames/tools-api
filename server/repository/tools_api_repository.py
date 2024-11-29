from server.database import db_connection # -> Para trabajar la base de datos
from server.database.models import ToolModel # -> Para trabajar la base de datos


class ToolsRepository:
    
    def __init__(self):
        self.db = db_connection.session

    def create(self, new_tool_dict: dict) -> dict:
        new_tool = ToolModel(**new_tool_dict)
        self.db.add(new_tool)
        self.db.commit()
        self.db.refresh(new_tool)
        return self.__to_dict(new_tool)

    def get_list(self, limit: int, offset: int) -> list[dict]:
        tools = self.db.query(ToolModel).order_by('id').limit(limit).offset(offset).all()
        return [self.__to_dict(tool) for tool in tools]

    def get_by_id(self, tool_id: int) -> dict | None:
        tool = self.__get_one(tool_id)
        if tool is None: return
        return self.__to_dict(tool)

    def update(self, id: int, new_tool_data: dict) -> dict | None:
        tool = self.__get_one(id)
        if tool is None: return
        for field in new_tool_data.keys():
            setattr(tool, field, new_tool_data[field] )
        self.db.commit()
        self.db.refresh(tool)
        return self.__to_dict(tool)

    def delete(self, id: int) -> bool:
        tool = self.__get_one(id)
        if tool is None: return False
        self.db.delete(tool)
        self.db.commit()
        return True

    def __get_one(self, tool_id: int) -> ToolModel | None:
        return self.db.query(ToolModel).filter_by(id=tool_id).first()

    def __to_dict(self, tool: ToolModel) -> dict:
        return {
            column.name: getattr(tool, column.name)
            for column in ToolModel.__table__.columns
        }
