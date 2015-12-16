__author__ = 'joe'
# -*- coding: utf-8 -*-

# 装饰器原理

def decorator_factory(enter_msg, exit_msg):
    def simple_decorator(f):
        def wrapper():
            print(enter_msg)
            f()
            print(exit_msg)
        return wrapper()
    return simple_decorator

@decorator_factory("Start", "End")
def hello():
    print("hello world")

hello