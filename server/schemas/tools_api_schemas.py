from datetime import datetime

from pydantic import BaseModel


class NewToolRequest(BaseModel):
    tool_name: str
    brand: str
    tool_type: str
    description: str
    location_in_warehouse: str
    status: str


class ToolRequest(BaseModel):
    tool_name: str | None = None
    brand: str | None = None
    tool_type: str | None = None
    description: str | None = None
    location_in_warehouse: str | None = None
    status: str | None = None


class ToolResponse(BaseModel):
    id: int
    tool_name: str
    brand: str
    tool_type: str
    description: str
    location_in_warehouse: str
    status: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
