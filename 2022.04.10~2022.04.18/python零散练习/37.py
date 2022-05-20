#转14.py
#高级变量类型list
"""
1,列表：在其他语言中通常叫数组
索引：又称为下标，就是数据在列表中的位置编号，如果超出范围，程序会报错 #索引是从0开始的！
"""
name_list = ["张三","李四","王五"]
#print(name_list[3])  超出索引范围，程序报错
#1.取值和取索引
print(name_list[0])
#2.修改
#name_list[位置] = 要修改的值
#例 name_list[0] = "lisi"

#3.增加
name_list.append("李四")#方法一：在末尾加
name_list.insert(4,4)#方法二：在指定位置加
print(name_list)

temp_list = ["q","w","e","r","t"]
name_list.extend(temp_list)#将temp_list添加到name_list
print(name_list)
#4.删除
name_list.remove("r")#从列表中删除指定数据
name_list.pop()#默认删除列表中最后一个元素
name_list.pop(0)#也可删除指定数据
print(name_list)
name_list.clear()#清空列表
print(name_list)

temp_list2 = ["1","2","3"]
#科普，不建议在list里使用
del temp_list2[0]#本质上将变量从内存中删除 注意：后续的代码就不能使用这个变量了  
# print(name_list)