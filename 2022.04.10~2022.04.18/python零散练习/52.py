#切片
#适用于字符串、列表、元组
#语法：字符串[开始索引：结束索引：步长]
num_str = "0123456789"
a = num_str[2:6]#2-5
print(a)
b = num_str[2:]#2-9
print(b)
c = num_str[0:6]#0-5
print(c)
d = num_str[:6]#0-5
print(d)
e = num_str[::2]#02468
print(e)
f = num_str[1::2]#13579
print(f)
g = num_str[-1]#9
print(g)
h = num_str[2:-1]#2-9
print(h)
i = num_str[-2:]#89
print(i)
j = num_str[-1::-1]#倒序
print(j)
k = num_str[::-1]#倒叙
print(k)
