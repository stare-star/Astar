# @Time  : 2019/6/8 0008 16:46
# @Author: LYX
# @File  : My_log.py

import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[ln:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
if __name__ == '__main__':

    logging.info('this is a loggging info message')
    logging.debug('this is a loggging debug message')
    logging.warning('this is loggging a warning message')
    logging.error('this is an loggging error message')
    logging.critical('this is a loggging critical message')

