# -*- coding: cp936 -*-
#----------------1. 列表-------------------#
# 列表是可变的mutable!

# 根据序列创建列表
l = list('python')
print l
# 赋值
l[0] = 'x'
print l
# 删除
del l[-1]
print l
#分片赋值
l[1:] = 'aaa'
print l
l[1:1] = 'bbb' #类似插入

# 重要函数
l.append(3) # 追加
a_count = l.count('a') # 统计某个元素出现的次数
l.index('a') # 找打第一个匹配值得下标
l.insert(2, 'x') # 插入
l.pop() # 移除最后一个，并返回
l.remove('a') # 移除第一个匹配值
l.reverse() # 反向列表，不返回值

#l.sort() # 会改变原来列表，并且不返回值
#b = a; # 只是单纯地将a和b指向了同一个列表，应该用 b = a[:]来拷贝

#v = sorted(a) #获得一配需列表的副本，不影响原来的列表
