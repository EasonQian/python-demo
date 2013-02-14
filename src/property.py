# -*- coding: utf-8 -*-
__metaclass__ = type
# 尽量使用property函数，而不是访问器方法！！！
class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setSize(self, size):
        self.width, self.height = size
    def __getSize(self):
        return self.width, self.height
    size = property(__getSize, __setSize) # 属性构造，隐藏访问器方法
    # 使得size的计算被隐藏起来
r = Rectangle()
r.width = 100
r.height = 200
print r.size
r.size = (500, 1000) # 500, 10000
print r.height


# 静态方法和类成员方法
class Myclass:
    @staticmethod # @操作符：列出decorators装饰器，可以修饰类或函数
    def smeth():
        print 'this is a static method'
    @classmethod
    def cmeth(cls):
        print 'this is a class method of', cls
    # 第二种定义的方式
    def smeth2():
        print 'this is another static method'
    smeth2 = staticmethod(smeth2)
      
Myclass.smeth()
Myclass.cmeth()
Myclass.smeth2()


# 拦截对象的"所有"特性的访问,要考虑好管理细节
class Rec():
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr(self, name, value): # 当试图给name赋值时会自动调用
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name): #会拦截包括self在内的特性访问，因此在内部访问self的时候，必须使用超类的__getattr__才是安全的，否则会造成死循环
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError
