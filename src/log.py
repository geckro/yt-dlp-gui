import logging

LOG_FILENAME = 'log.log'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOGGING_LEVELS = {'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR, 'debug': logging.DEBUG}

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format=LOG_FORMAT
)


def log(level: str, message: str) -> None:
    """
    Log a message with the specified severity level.
    Parameters:
    - level (str): The severity level of the log ('info', 'warning', 'error', 'debug')
    - message (str): The message to be logged
    """
    logging.log(LOGGING_LEVELS[level], message)
