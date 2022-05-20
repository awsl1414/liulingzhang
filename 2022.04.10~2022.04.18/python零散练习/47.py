#循环遍历字典
xiaoming_dict = {"name":"小明",
"qq":"123456",
"phone":"10086"}
#变量a是每一次循环中，获取到的键值对的key
for a in xiaoming_dict:
    print("%s - %s"%(a,xiaoming_dict[a]))
for b in xiaoming_dict:
    print(b)
print(xiaoming_dict)
xiaoming_dict["email"] = "xiaoming@qq.com"#向字典中添加数据
print(xiaoming_dict)
