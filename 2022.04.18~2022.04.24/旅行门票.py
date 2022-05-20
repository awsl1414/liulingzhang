# 4岁以下免费；
# 4~18岁收费5美元；
# 18岁（含）以上收费10美元。

age = int(input("请输入旅客的年龄："))
if age < 4:
    print("不收费")
elif 4 <= age <18:
    print("收费￥5")
else:
    print("收费￥10")

#优化
age = int(input("请输入旅客的年龄："))
if age < 4:
    price=0
elif 4 <= age <18:
    price=5
elif age >= 18:
    price=10
print("收费"+str(price)+"元。")