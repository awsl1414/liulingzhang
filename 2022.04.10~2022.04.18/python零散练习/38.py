name_list = ["张三","李四","王五","张三"]
len(name_list)#统计列表中元素的总数
print(len(name_list))

name_list.count("张三")#统计某一变量出现的次数
print(name_list.count("张三"))

name_list.remove("张三")#删除第一次出现的数据，如果数据不存在，程序会报错
print(name_list)
