import os
import logging
from logging.handlers import TimedRotatingFileHandler


def config_logger(debug_level: bool) -> None:
    LOGS_PATH = './logs'
    # HACER: Checkear si existe la carpeta logs
    if not os.path.exists(LOGS_PATH):
        os.makedirs(LOGS_PATH)
    
    log_filename = LOGS_PATH + '/tools-api.log'
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if debug_level else logging.INFO)

    handler = TimedRotatingFileHandler(
        log_filename,
        when= 'midnight',
        interval= 1,
        backupCount= 0,
    )
    handler.suffix = '%Y%m%d'

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt= '%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)