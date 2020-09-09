from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG
import constants.basic

class Logger:
    def __init__(self, name=__name__):
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

        # stdout
        handler = StreamHandler()
        handler.setLevel(constants.basic.LOG_STGOUT_LEVEL)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        from datetime import datetime
        nowData = datetime.now().strftime('%Y%m%d')

        # file
        handler = handlers.RotatingFileHandler(filename = constants.basic.LOG_FIlE_DIR + nowData +'.log',
                                               maxBytes = 1048576,
                                               backupCount = 3)
        handler.setLevel(constants.basic.LOG_FILEOUT_LEVEL)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)