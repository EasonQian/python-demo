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

#name = ''
#while not name or name.isspace():
#	name = raw_input('please enter your name: ')
#print 'hello ' + name

# for
for number in range(1, 10): # slice, 1 included and 10 not included!!
	print number

# for and map
d = {'x':1, 'y':2, 'z':3} # order is not certain
for key, value in d.items():
	print key, 'corresponds to ', value

# 并列迭代
names = ['qianwei','helu','wangdandan','cuijingwen']
ages = [22, 21, 22, 23]
#for i in range(len(names)): # xrange不会一次性创建整个序列，而是一个一个创建，在数据量很大的时候推荐使用！！
#	print names[i], 'is', ages[i], 'years old'

# zip 压缩两个序列
print zip(names, ages) 
for name, age in zip(names, ages): # 并行迭代，在循环中解包！！！
	print name, 'is', age, 'years old'
# 当最短的序列用完的时候，压缩结束	
print zip(range(5), xrange(100000))

# enumerate: 索引-值的迭代
strings = ['xxx', 'yyy', 'xxx']
for index, string in enumerate(strings):
	if 'xxx' in string:
		strings[index] = 'change this'
print strings

# 列表推倒式：利用其他列表创建新列表
import math
print [math.pow(x, 2) for x in range(5)]
print [(x, y) for x in range(5) for y in range(3)] # liek enum
