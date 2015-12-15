__author__ = 'joe'
#!/usr/bin/env python

import os
import pickel

class FileDescr(object):
    saved = []

    def __init__(self, name = None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, "%r used before assignment" % self.name

        try:
            f = open(self.name, 'r')
            val = pickel.load(f)
            f.close()
            return val
        except(pickle.InpicklingError, IOError,EOFError,AttributeError,ImportError,IndexError),e:
            raise AttributeError,"could not read %r: %s" % self.name

    def __set__(self, obj, val):
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(val, f)
                FileDescr.saved.append(self.name)
            except(TypeError, pickle.InpicklingError), e:
                raise AttributeError, "could not pickle %r" % self.name
            finally:
                f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except(OSError,ValueError), e:
            pass
