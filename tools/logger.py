import logging

class AppLog:
    def __init__(self) -> None:
        pass
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    
    def info(self, stringInfo):
        logging.info(stringInfo)

    def warning(self, stringInfo):
        logging.warning(stringInfo)

    def error(self, stringInfo):
        logging.error(stringInfo)

    def info(self, stringInfo):
        logging.debug(stringInfo)

    def critical(self, stringInfo):
        logging.critical(stringInfo)

    def exception(self, stringInfo):
        logging.exception(stringInfo)