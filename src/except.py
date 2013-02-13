# -*- coding: utf-8 -*-
__metaclass__ = type

class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try: # try clause
            return eval(expr)
        except (ZeroDivisionError, TypeError) as e: # use block to catch exceptions
            if self.muffled:
                print 'Division ...'
                print e # print error message
            else:
                raise # use raise to occur exception