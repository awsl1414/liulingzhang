#转37.py
#list
#Python内置的一种数据类型是列表：list是一种有序的集合，可以随时添加和删除其中的元素。


friends = ['zhangshan','lisi','wangwu']#friends就是一个list
print(friends)


#用len() 可以获取list元素的个数
len(friends)
#输出为3
len(friends)


#用索引来访问list中的每一个位置的元素，记得索引是从0开始的
#输出为'zhangshan'
friends[0]
#输出为'lisi'
friends[1]


#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) -1
#输出为'wangwu'
friends[-1]
#倒数第二个
friends[-2]
#倒数第三个
friends[-3]
#倒数第四个 倒数第4个就越界了
#friends[-4]
"""
倒数第四个  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
"""


#list是一个可变的有序表

#在list末尾添加'mowei'
friends.append('mowei')
#输出为['zhangsan','1','lisi' ...]
friends.insert(1,'1')


#要删除list末尾的元素，用pop()
#friends.pop('mowei')
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
#friends.pop(1,'1') 输出为 ['zhangshan','lisi','wangwu']


#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
friends[1] = '1'#输出为['zhangsan','1','lisi' ...]


#list里面的元素的数据类型也可以不同
M = ['Apple', 123, True]


#list元素也可以是另一个list

#s可以看成是一个二维数组，类似的还有三维、四维……数组
s = ['python', 'java', ['asp', 'php'], 'scheme']


#tuple 元组 tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
#classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
#tuple和list的表面区别：list:[] tuple:()
#意义：因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
#当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

#t = (1)#输出为1    定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
#t = (1,)  输出为(1,) #Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号


b = ('a', 'b', ['A', 'B'])
#将位于2位的list中0位替换为X
b[2][0] = 'X'
#将位于2位的list中1位替换为Y
b[2][1] = 'Y'
#输出为('a', 'b', ['X', 'Y'])



