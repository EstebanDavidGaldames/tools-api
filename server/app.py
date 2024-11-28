from fastapi import FastAPI

from .api import api_router


app = FastAPI()

app.include_router(api_router)


@app.on_event('startup')
async def startup_event():
    print('\033[92m', 'API Iniciada', '\033[0m')

@app.on_event('shutdown')
def shutdown_event():
    print('\033[91m', 'API Finalizada', '\033[0m')
