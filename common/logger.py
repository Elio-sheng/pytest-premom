import logging
import time
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Get the base path of the current file

# Define the log file path
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    """
    Class to handle logging.
    """

    def __init__(self):
        """
        Initialize the Logger class.
        """
        self.logname = os.path.join(
            LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(
            self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

# if __name__ == '__main__':
#     logger.info("---start test---")
#     logger.debug("---test end---")
