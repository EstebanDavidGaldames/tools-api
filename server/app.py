#import logging

from fastapi import FastAPI

from .api import api_router


#logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(api_router)


#@app.on_event('startup')
#async def startup_event():
#    print('\033[92m', 'API Iniciada', '\033[0m')
#    logger.debug('Mensaje de debug.')
#    logger.info('Mensaje de info.')
#    logger.warning('Mensaje de warning.')
#    logger.error('Mensaje de error.')
#    logger.critical('Mensaje de critical.')

#@app.on_event('shutdown')
#def shutdown_event():
#    print('\033[91m', 'API Finalizada', '\033[0m')
