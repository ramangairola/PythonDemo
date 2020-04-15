import logging

def test_Demo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log")
    formatHandler = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
    fileHandler.setFormatter(formatHandler)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug")
    logger.critical("Critical")
