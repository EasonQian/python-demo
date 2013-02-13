## format string with given value
#format = "hello, %s!"
#value = ("world")
#rst = format % value
#print rst

## format float number
#format = "Pi with three decimals: %.3f"
#import math
#print format % math.pi

## join, must be string!
#seq = ['1', '2', '3', '4']
#sep = '+'
#rst = sep.join(seq) #join list
#print rst
#dirs = '','usr','bin','env'
#rst = '/'.join(dirs)
#print repr(rst)
#print 'C:' + '\\'.join(dirs)

## split: split string into list
#rst = '1+2+3+4'.split('+')
#print rst
#rst = '1 2 3 45 '.split() # no param is given, blank is indicated to be the spliter
#print rst

## lower
#rst = 'THIS'.lower()
#print rst

## title: first letter of all word will be upcase
#rst = 'this is a title'.title()
#print rst

## replace
#rst = 'this is a test'.replace('is', 'is not')
#print rst

# translate: like replace, but can replace more than one char
#from string import maketrans # i'm a little bit confused why this cannot import???
#table = maketrans('cs', 'kz') #trans table, change c to k and change s to z
#print len(table)
#rst = 'this is an change test'.translate(table)
#print rst


## strip: like trim in js,
#rst = '   internal whitesapce is kept  '.strip()
#print rst
#rst = '## strip given chars at head and end **'.strip('#*')
#print rst


## composite demo
names = ['gumby', 'smith', 'eason']
name = 'gumby '
if name in names: print 'Found it1'
if name.strip() in names: print 'Fount it2'