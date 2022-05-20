#在函数内部修改全局变量
num  = 10
def demo1():
    #希望修改全局变量 - 使用global声明变量即可
    #global会告诉后面的变量是全局变量
    global num
    num = 99
    print("demo1 ==> %d"%num)
def demo2():
    print("demo2 ==> %d"%num)
demo1()
demo2()
