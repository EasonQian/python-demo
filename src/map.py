# map
phoneBook = {'qianwei':'1234', 'cuijingweng':'2345'}
print phoneBook['qianwei']

# dict: key-value pairs
items = [('name', 'EasonQian'),('age', 23)] # use list to create map
d = dict(items)
print d['name']
d = dict(name='EasonQian', age='23') # use keyword to create map
print d['name']

# primary dict functions
len_of_d = len(d) # return count of items of d
print len_of_d
del d['age'] # delete item whose key = ?
print d
flag = 'name' in d # check if d contains key = ?
print flag 

#
# x = [] # list
# x[2] = 'wrong' # this is wrong, for x[2] is not existed.
x = {} # map
x[2] = 'right' # this is right, map will automatically add a pair (2, 'right')

# clear, none return value
a = dict(name="EasonQian", age="23")
a.clear()
print a # a is empty


# copy and deep copy
# this is very important:
# in python, object is passed through reference!!!
# 1. copy(shalow copy): copy an object, but innner property is reference
# 2. deepcopy: copy ultimately to another object
# e.g.
m = {'name':'admin', 'machines':['ma1', 'ma2', 'ma3']}
n = m.copy()
n['name'] = 'user'
print 'm is not affected'
print m, n
n['machines'].append('ma4')
print 'm is affected'
print m, n

# haha, double-screen, but no proper keyboard.


#from keys: create new dict, all values are None
ff = {}.fromkeys(['name', 'age']) # or dict.fromkeys()
print ff
# you can provide your own default value
ff = {}.fromkeys(['name', 'age'], '(unknown)')
print ff

# get, prevent the fault expr when access the unexisted item using dict[]
print d.get('nothisitem') # None, rather fault expr
# add a default value when access a possible unexisted item
print d.get('nothisitem', 'no this key') #!!!!!!! very useful

# has_key
d = {}
print d.has_key('name') # False

# items and iteritems
d = {'title':'python web app', 'url':'www.baidu.com'}
print d.items() # list:(key, value)
it = d.iteritems() # more effective!!!
print list(it) # convert iterator to list

# keys and iterkeys: like above

# values nad itervalue: above

# pop: return value from given key, and delete key from map
print d.pop('url')
print d

# popitem: randomly remove item!!!
d['name'] = 'python'
print d
print d.popitem() # random!!!

# setdefault
e = {}
e.setdefault('name', 'N/A')
print e
e['name'] = 'EasonQian'
print e.setdefault('name', 'N/A') # already has a value, return value in the map!!
print e

# update: use map1 to update map2, add or change already existed key 
