# -*- coding: cp936 -*-
# print 
print 'aa', 'bb' # more than one print
print 'hello', # use semicolom to prevent change another line
print 'world' # hello world

# import 
#from math import *
#import math
#import math as alias # another name

# assign value!!!
x, y, z = 1, 2, 3 # assign more than one values!
print x, y, z
x, y = y, x # exchange two values!
# this is sequence unpacking
values = 1, 2, 3
print values
x, y, z = values
print x 

# true and false
print True == 1 # True
print False == 0 # True
True + False + 42 # 43

# is: must be the same object
x = [1, 2, 3]
y = [2, 4]
print x is not y # True, for they are not the same object
## ! so, use == to determine value equation,  use is to determine whether is the same object

# bool operation: and, or, not: fast-fail property!!
# a if b else c: if b is true, return a, else return c!!


# assert 0 < a < 10

# while: use tab to control logical process 
x = 1
while x <= 3:
	print x
	x += 1

name = ''
while not name or name.isspace():
	name = raw_input('please enter your name: ')
print 'hello ' + name




