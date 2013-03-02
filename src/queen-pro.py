# -*- coding: utf-8 -*-
__metaclass__ = type

##############################################
# this is a good exmaple of python yield usage
# yield one value one time and the process stop
# at that point, and wait for next invoking
# just like iterator
##############################################

# 定义冲突函数
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i): # 水平距离为0(同一列)或等于垂直距离(一条对角线上)
            return True
    return False

#def queens(num=8, state=()):      
#    if len(state) == num -1:
#        for pos in range(num):
#            if not conflict(state, pos):
#                yield (pos,)
#    else:
#        for pos in range(num):
#            if not conflict(state, pos):
#                for result in queens(num, state+(pos,)):
#                    yield (pos,) + result

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,)+result
# test:
print list(queens(4, (1, 3, 0)))
print list(queens(4))
print len(list(queens(8)))
