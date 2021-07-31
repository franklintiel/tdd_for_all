"""
Logger class
"""
import os
import logging

current_dir = os.getcwd()
logger_path = os.path.join(current_dir, '..', 'files/logs')

LOGGER_FILE_PATH = "{0}/tasks.log".format(logger_path)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt="%m-%d %H:%M",
                    filename=LOGGER_FILE_PATH)

class Logger:
    """
    Main class to generate loggers
    """
    def __init__(self, module_name):
        self.module_name = module_name
        self.logger = logging.getLogger(self.module_name)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)
