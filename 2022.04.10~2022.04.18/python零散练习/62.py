#递归函数
#定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#递归的优点：定义简单，逻辑清晰
#理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
fact(5)
5 * fact(4)
5 * (4 * fact(3))
5 * (4 * (3 * fact(2)))
5 * (4 * (3 * (2 * fact(1))))
5 * (4 * (3 * (2 * 1)))
5 * (4 * (3 * 2))
5 * (4 * 6)
5 * 24
120
'''
#注意：防止栈溢出
#解决方法：尾递归优化

#尾递归定义：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(10000,1))
'''
fact_iter(5, 1)
fact_iter(4, 5)
fact_iter(3, 20)
fact_iter(2, 60)
fact_iter(1, 120)
120
'''