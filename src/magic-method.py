# -*- coding: utf-8 -*-

__metaclass = type
# 构造方法
class FooBar:
    def __init__(self, value=42): # use __init_ as the constructor
        self.somevar = value

f = FooBar() # atomically call __init__ method
print f.somevar # 42
f = FooBar('this is a constructor argument')
print f.somevar # this is a constructor argument

# 必须显示调用超类的构造方法，来进行子类的构造函数初始化
class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah'
            self.hungry = False
        else:
            print 'No thanks'
class SomeBird(Bird):
    def __init__(self):
#        Bird.__init__(self) # 1: 调用超类的__init__方法，unbound method?
        # super只能用于python的新类中，即所有的类都要继承自父类(或object)，否则会报错！！！
        super(SomeBird, self).__init__() # 2: 调用super方法，可以认为super返回了所有的超类
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
sb = SomeBird()
sb.eat()


# 子类化内建类型
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.count = 0
    def __getitem__(self, index): # 返回与所给建对应的值
        self.count += 1
        return super(CounterList, self).__getitem__(index)
c1 = CounterList(range(3))
print c1
print c1.count # 0
print c1[1] + c1[2]
print c1.count # 2


# 类似的魔法方法还有
#__len__(self)
#__getitem__(self, key)
#__setitem__(self, key, value)
#__delitem__(self, key)

