__author__ = 'sara'

import logging
import os
import time

prjDir = os.path.dirname(os.path.dirname(__file__))
__result_path = os.path.join(prjDir, "result")
log_path = os.path.join(__result_path, (time.strftime('%Y%m%d%H%M%S', time.localtime())))


def __set_log():
    # result_path = os.path.join(prjDir, "result")
    if os.path.exists(log_path) is False:
        os.makedirs(log_path)

    # #create a logger
    # logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    #
    # # create handler,write log
    # fh = logging.FileHandler(os.path.join(log_path, "outPut.log"))
    # out = logging.StreamHandler()
    # # Define the output format of formatter handler
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - line%(lineno)d: %(message)s')
    # fh.setFormatter(formatter)
    # fh.setLevel(logging.DEBUG)
    # out.setFormatter(formatter)
    # out.setLevel(logging.DEBUG)
    #
    # logger.addHandler(fh)
    # logger.addHandler(out)

    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(os.path.join(log_path, "outPut.log"))
    fh.setLevel(logging.DEBUG)
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

# __set_log()

__all__ = ['bsnsCommon', 'DRIVER', 'get_element', 'get_elements', 'ReadConfig', 'HTMLTestRunner']
from . import bsnsCommon
from .common import get_element, get_elements, DRIVER, ReadConfig
from .HTMLTestRunner import HTMLTestRunner
