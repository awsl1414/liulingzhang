#字符串的定义
#
str1 = "hello python hello world"
str2 = '我的外号是"大西瓜"'
#索引
a = str1[0]
print(a)
#遍历
for b in str1:
    print(b)
#常用方法
#len
c = len(str1)
print(c)
#.count 统计某一个小字符串出现的次数
d = str1.count("llo")
print(d)
#.index 某一个子字符串的位位置
e = str1.index("python")
print(e)

