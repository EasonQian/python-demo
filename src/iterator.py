# -*- coding: utf-8 -*-

__metaclass__ = type

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self): # 迭代器实现next方法
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self): # 迭代器实现__iter__方法,返回迭代器本身
        return self
# 实现了next和__iter__方法的对象是可迭代对象
fib = Fibs()
for f in fib: # 可以再for循环中直接使用迭代器本身了
    if f > 1000:
        print f
        break
    
# 将迭代器转化为序列
class TestIter:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = TestIter()
print list(ti) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]