import inspect
import logging

import allure


def customLogger():
    # 1. get class/method name yang manggil customer logger ini
    logName = inspect.stack()[1][3]

    # 2. create object logging
    logger = logging.getLogger(logName)

    # 3. Set level
    logger.setLevel(logging.DEBUG)

    # 4. create filehandler to save the logs
    fileHandler = logging.FileHandler("../reports/AppiumFramework.log".format(logName), mode='a')

    # 5. set loglevel fo filehandler
    fileHandler.setLevel(logging.DEBUG)

    # 6. Create formatter
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%y-%m-%d %I:%M:%S %p %A')

    # 7. set formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # 8. add file handler to logging
    logger.addHandler(fileHandler)

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
