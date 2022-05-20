#定义一个求一元二次方程的根的函数
import math
def quadratic(a,b,c):
    n1 = b**2-4*a*c
    if n1 < 0:
        print("该方程没有实根")
    else:
        n2= math.sqrt(n1)
        x1 = (-b+n2)/(2*a)
        x2 = (-b-n2)/(2*a)
        if x1 ==x2:
            print("该方程有且仅有一个根：%f"%x1)
        else:
            print("该方程的一个根为：%s"%x1)
            print("该方程的另一个根为：%s"%x2)
a = quadratic(1,1,1)
print(a)