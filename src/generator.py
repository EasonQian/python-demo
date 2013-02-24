# -*- coding: utf-8 -*-
__metaclass__ = type

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element # 包含yield的函数就是一个generator,改函数不同于return，yield不会立即返回，而是最后返回多个值            
# e.g.
nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print num
# or
print list(flatten(nested))

# 递归生成器
# !这个函数对于类似字符串的对象不适用，会导致把字符串当成一个序列，不能引发TypeError异常的无穷递归发生
def flatten2(nested):
    try:
        # 检查是不是字符串，不能迭代类似字符串的对象
        try: 
            nested + '' 
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
# e.g.
print list(flatten2([[[1], 2], 3, 4, [5,[6,7]], 8]))
print list(flatten2(['foo', ['bar', ['baz']]]))