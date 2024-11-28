from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base_model import ToolBaseModel


class ToolModel(ToolBaseModel):
    __tablename__ = 'tools'
    
    tool_name: Mapped[str] = mapped_column(String(30), nullable=False)
    brand: Mapped[str] = mapped_column(String(20), nullable=False)
    tool_type: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(120), nullable=False)
    location_in_warehouse: Mapped[str] = mapped_column(String(10), nullable=False)
    status: Mapped[str] = mapped_column(String(10), nullable=False)
