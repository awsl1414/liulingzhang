def print_line(char,times):
    print(char * times)
print_line("-",50)

def print_lines(char,number):    #模块名也是标识符！
    a = 0
    while a < 5:
        print_line(char,number)   #嵌套使用函数
        a += 1
print_lines("/",50)