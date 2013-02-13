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

# class namespace
