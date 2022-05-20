#统计键值对数量
xiaoming_dict = {"name":"小明",
"age":"18"}
print(len(xiaoming_dict))
#合并字典
temp_dict = {"weight":60}
xiaoming_dict.update(temp_dict)
#如果被合并的字典中包含已经存在的键值对时，会覆盖原有键值对
print(xiaoming_dict)
#清空字典
xiaoming_dict.clear()
print(xiaoming_dict)