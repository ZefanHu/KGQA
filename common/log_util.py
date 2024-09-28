import logging
import os
import threading
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from logging import StreamHandler


def init_logger(log_path: str):
    logging.getLogger("urllib3.connectionpool").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)
    logging.getLogger("connectionpool").setLevel(logging.INFO)
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # init root logger
    formatter = logging.Formatter('[%(asctime)s %(levelname)s %(lineno)d]: %(message)s')

    time_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, "main.log"), when='D', encoding='utf-8')
    time_handler.setFormatter(formatter)
    time_handler.setLevel(logging.INFO)

    logger = logging.getLogger()
    logger.addHandler(time_handler)
    logger.addHandler(StreamHandler())
    logger.setLevel(logging.INFO)
    logging.getLogger('main').setLevel(logging.INFO)

    return logger


def get_thread_logger():
    """
    得到每个线程独有的log
    :param k:
    :return:
    """

    return logging.getLogger(f'node-{threading.current_thread().name}')


def get_main_logger():
    return logging.getLogger("main")

# log = get_thread_logger()
