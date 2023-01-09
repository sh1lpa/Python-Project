import sys
import logging

def error_handling():
    return f'{sys.exc_info()[0]} with {sys.exc_info()[1]} at line {sys.exc_info()[2].tb_lineno}'


try:
    a+b
except Exception as e:
    logging.error(error_handling())