# @Time  : 2019/6/8 0008 16:46
# @Author: LYX
# @File  : My_log.py

# import logging
#
# logging.basicConfig(level=logging.INFO,
#                     filename='log.log',
#                     encoding='utf-8',
#                     format='%(asctime)s - %(filename)s[ln:%(lineno)d] - %(levelname)s: %(message)s')
# logger = logging.getLogger(__name__)
# # use logging

import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
BASIC_FORMAT = '%(asctime)s - %(filename)s[ln:%(lineno)d] - %(levelname)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
chlr = logging.StreamHandler()  # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
fhlr = logging.FileHandler('star.log',encoding='utf-8')  # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)


if __name__ == '__main__':
    logger.info('this is info')
    logger.debug('this is debug')
