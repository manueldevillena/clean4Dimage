import datetime as dt
import logging


def set_up_logger(path: str, log_in_file: bool=True):
    """Sets up the logger.

    Args:
    -----
        path: path to store the log
        log_in_file: whether or not to store the log

    Returns:
    --------
        logger

    """
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rootLogger = logging.getLogger()

    if rootLogger.hasHandlers():
        for hdlr in rootLogger.handlers[:]:  # remove all old handlers
            rootLogger.removeHandler(hdlr)
    if log_in_file:
        fileHandler = logging.FileHandler(f'{path}/logfile_{dt.datetime.utcnow()}.log')
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    rootLogger.setLevel(logging.INFO)

    return rootLogger
