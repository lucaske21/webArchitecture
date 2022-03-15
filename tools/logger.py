import logging
from typing import List

class AppLog:
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    
    def info(self, input: List[str]):
        logging.info(" ".join(map(str, input)))

    def warning(self, input: List[str]):
        logging.warning(" ".join(map(str, input)))

    def error(self, input: List[str]):
        logging.error(" ".join(map(str, input)))

    def debug(self, input: List[str]):
        logging.debug(" ".join(map(str, input)))

    def critical(self, input: List[str]):
        logging.critical(" ".join(map(str, input)))

    def exception(self, input: List[str]):
        logging.exception(" ".join(map(str, input)))