# -*- coding: utf-8 -*-
__metaclass__ = type # 使用新式类

class Person:
    act = 'speaking'
    __privateAttr = 'this is private'
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print 'This is', self.name, self.act
    def __inaccessible(self): # 在函数名称前面加上双下划线，私有化函数
        print 'bet you cannot see it'
        
p = Person()
p.setName('Eason Qian')
p.greet()
#p.__inaccessible() # cannot access private function
#p.__privateAttr # cannot access private attribute

# super class
class Su:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked] # fantastic expression!!!
class Child(Su): # use () to inherit from super class
    def init(self): # over-write 
        self.blocked = ['self']
    def filter(self, sequence): # over-write 
        # ... add logic process for Child class
        pass
    
    
flag = issubclass(Child, Su) # determine if a class is sub of another class
print flag # Ture

obj = Child()
# 获取基类
print Child.__bases__ # (<class '__main__.Su'>,)
# 获取对象所属的类
print obj.__class__ # <class '__main__.Child'>


print isinstance(obj, Child) # True
print isinstance(obj, Su) # True


# 多继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print 'hello, my value is', self.value
class TalkingCal(Calculator, Talker): # multi-inheritance
    pass 

tc = Talker()
print hasattr(tc, 'talk') # True, tc对象含有一个talk特性(方法)

