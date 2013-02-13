# -*- coding: utf-8 -*-
# 构造斐波那契数列
#fibs = [0, 1]
#for i in range(8):
#    fibs.append(fibs[-2] + fibs[-1])
#print fibs

def fib(num):
    '斐波那契数列生成器' # this is document string文档字符串，作为函数的注解
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

print fib(10)
print fib.__doc__ # 显示文档字符串
help(fib)

# 如果函数没有return，则默认返回的是None
def f_without_return():
    pass
print f_without_return() # None

# function parameter properties
def not_change(n):
    n = 'change'
name = 'EasonQian'
not_change(name)
print name # not changed, this is passed by value

def change(n):
    n[0] = "change"
names = ['EasonQian', 'EricSun']
change(names)
print names # changed, this is passed by reference, if want not changed, copy the entire list using ano = names[:]


# use init function
storage = {}
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
init(storage)
print storage


# default param
def de_f(name="Eason"):
    print name
de_f('Qian')
de_f() # default name will be printed

# 多个参数， 星号：收集其余的位置参数
def m_param(*params):
    print params
m_param(1, 2, 3) # 以元组的形式打印出来了，即参数前的星号把所有的值都放在一个元组中了，

## intergrate demo
def story(**key_words): # define a fun to receive 关键字参数
    return 'Once upon a time, there was a ' \
        '%(job)s called %(name)s.' % key_words
print story(job='king', name='Qian')
#print story(job='king') # key error!!!

# about global
x = 1
def g_fun():
    global x # declare x is global,重新绑定全局变量
    x = x + 1
g_fun()
print x
# 使用globals()['parameter']获取全局变量

# binary search
def bi_search(sequence, number, left=0, right=None):
    'binary search in python'
    if right == None: 
        right = len(sequence) - 1
    if left == right: 
        assert number == sequence[right]
        return right
    else:
        middle = (left + right) // 2 # 整数除法！！！
        if number > sequence[middle]:
            return bi_search(sequence, number, middle+1, right)
        else: 
            return bi_search(sequence, number, left, middle)
seq = [3,53,62,12,67,23,71,23]
seq.sort(cmp=None, key=None, reverse=False)
index = bi_search(seq,67)
print index

