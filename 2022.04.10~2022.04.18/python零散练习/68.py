#交换数字
a = 6
b = 100
# #解法一
# c = a
# a = b
# b = c
# print(a,b)
#解法二 -不使用其他的变量
a = a+b
b = a-b
a = a-b
print(a,b)
#解法三 -python专属
#等号右边是元组，只是括号被省略
# a,b = b,a+b
# print(a,b)