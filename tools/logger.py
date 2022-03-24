import logging
import colorlog
import sys
from typing import List

class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%d-%b-%y %H:%M:%S')
        return formatter.format(record)

class AppLog:
    def __init__(self) -> None:
        self.rootLogger = logging.getLogger()
        self.rootLogger.setLevel(logging.DEBUG)
        # self.fmt = logging.Formatter('%(asctime)s - %(levelname)-8s |%(name)-12s: - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        self.fmtStr = '%(asctime)s - %(levelname)-8s |%(name)-12s: - %(message)s | %(filename)s:%(lineno)d'
        self.consoleHandler = logging.StreamHandler()
        self.customFmt = CustomFormatter(self.fmtStr)
        self.consoleHandler.setFormatter(self.customFmt)
        self.rootLogger.addHandler(self.consoleHandler)

        # logging.basicConfig(format='%(asctime)s - %(levelname)-8s |%(name)-12s: - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    
    def info(self, input: List[str]):
        self.rootLogger.info(" ".join(map(str, input)))

    def warning(self, input: List[str]):
        self.rootLogger.warning(" ".join(map(str, input)))

    def error(self, input: List[str]):
        self.rootLogger.error(" ".join(map(str, input)))

    def debug(self, input: List[str]):
        self.rootLogger.debug(" ".join(map(str, input)))

    def critical(self, input: List[str]):
        self.rootLogger.critical(" ".join(map(str, input)))

    def exception(self, input: List[str]):
        self.rootLogger.exception(" ".join(map(str, input)))