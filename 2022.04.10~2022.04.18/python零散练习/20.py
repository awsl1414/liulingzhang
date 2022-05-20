print("今天发工资吗？")
a = input("请输入yes或者no：")
if a == "yes":
    print("请先还信用卡,并思考还有剩余吗，有请输入yes，没有请输入no")
    a = input("请输入1或者2")
    if a == "1":
        print("又可以happy了！")
    else:
        print("噢，no！")
else :
    print("盼工资")   
