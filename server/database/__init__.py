from server.configs import app_settings
from .database_connections import DatabaseConnection
from .models import ToolBaseModel


db_connection = DatabaseConnection(app_settings.DB_CONN)


def create_table():
    ToolBaseModel.metadata.create_all(bind=db_connection.engine)
