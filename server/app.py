from fastapi import FastAPI

from .api import api_router
from .database import db_connection, create_table


app = FastAPI()

app.include_router(api_router)


@app.on_event('startup')
async def startup_event():
    if db_connection.connect():
        create_table()

@app.on_event('shutdown')
def shutdown_event():
    db_connection.disconnect()
