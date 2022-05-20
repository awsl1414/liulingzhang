#元组
info_tuple = ("zhangsan",18,1.75)
a = info_tuple[0]
empty_tuple = ()#定义空元组
single_tupe = (1,)#定义只包含一个数字的元组

for b in info_tuple:
    #使用格式化字符串拼接 b 这个变量不方便
    #因为元组中通常保存的数据类型是不同的
    print(b)

