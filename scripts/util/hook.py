# -*- coding: utf-8 -*-
import inspect

def cmd(arg=None):
    def wrap(func):
        if not hasattr(func, "_hook"):
            func._hook = True
        if not inspect.isfunction(arg) and not hasattr(func, "_command"):
            func._command = arg
        return func

    if inspect.isfunction(arg):
        return wrap(arg)
    else:
        return wrap
