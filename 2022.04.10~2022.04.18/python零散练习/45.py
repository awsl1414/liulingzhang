xiaoming_dict = {"name":"小明"}
#取值
print(xiaoming_dict["name"])
#增加/修改
xiaoming_dict["age"] = 18
print(xiaoming_dict)
xiaoming_dict["name"] = "小小明"#如果key存在，会修改已存在的键值对，没有则会添加
#删除
xiaoming_dict.pop("name")
print(xiaoming_dict)


