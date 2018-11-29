#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date : 2018-11-29
# Author : wuchongyao
# wcy_log.py


import logging
import os


BASE_PATH, _ = os.path.split(os.path.abspath(__file__))
LOG_DIR = BASE_PATH + '\wcy.log'


def wcy_log(logger_name='WCY-LOG', log_file=LOG_DIR, level=logging.DEBUG):
    # 创建 logger对象
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)  # 添加等级

    # 创建控制台 console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 创建文件 handler
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')

    # 创建 formatter
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

    # 添加 formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把 ch， fh 添加到 logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def main():
    # print(BASE_PATH)
    # logger = wcy_log()
    # logger.error("test log")
    pass

if __name__ == '__main__':
    main()
