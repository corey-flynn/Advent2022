import logging
from functools import wraps
from time import time

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
LOGGER = logging.getLogger()


def timing(f: callable):
    """
    https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    :param f: function
    :return:
    """
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        LOGGER.info(f'func:{f.__name__} took: {te-ts:2.4f} sec')
        return result
    return wrap


def range_inc(*args):
    """
    range including the max number
    :param args: same arguments passed to range builtin
    :return: range generator
    """
    args = list(args)
    if len(args) >= 1:
        args[1] += 1
    else:
        args[0] += 1
    return range(*args)
