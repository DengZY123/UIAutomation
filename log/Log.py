import logging
import os
import time

log_path = "D:/PythonWorkSpace/UIAutomation/log"

class Logger():

    def __init__(self,logger,CmdLevel,FileLevel):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

        self.LogFileName = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

if __name__ == "__main__":
    logger = Logger("FOX",CmdLevel=logging.INFO,FileLevel=logging.DEBUG)
    logger.debug("debug message")
    logger.info("info message")






