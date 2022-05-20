#注意：在开发时，应该把模块中所有的全局变量-
#-定义在所有函数上方，保证所有函数都能正确的被访问
gl_num = 10
gl_title = "试验"
def demo():
    num = 99
    print("%d"%gl_num)
    print("%s"%gl_title)
demo()
