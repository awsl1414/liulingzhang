#石头剪刀布
import random #导入random模块
a = int(input("请选择要出的拳头 石头(1) 剪刀(2) 布(3):"))
b = random.randint(1,3) #生成随机数
if ((a == 1 and b == 2)
or(a == 2 and b == 3)
or(a == 3 and b == 1)):
    print("你赢了")
elif a == b:
    print("平局")
else:print("你输了")
