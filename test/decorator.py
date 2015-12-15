__author__ = 'joe'

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func._name_
        return func(*args, **kw)
    return wrapper