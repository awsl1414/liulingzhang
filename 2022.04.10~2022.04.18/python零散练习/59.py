
#set
from math import remainder


a = set([1,2,3,4])              #语法：x = set([])
print(a)
a.add(5)                        #添加指定key
print(a)
a.remove(4)                     #移除指定key
print(a)
b = set ([0,2,3,3,3,4,4,4])     #重复元素在set中自动被过滤
print(b)
c = a & b                       #set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
print(c,1)