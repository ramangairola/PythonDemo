import logging


class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        formatHandler = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        fileHandler.setFormatter(formatHandler)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
