#多值参数
def demo(num,*nums,**person):   #一个*是添加元组，两个*是添加字典   一般定义：(元组：*args,字典：*kwargs)
    print(num)
    print(nums)
    print(person)
demo(1,)
demo(1,2,3,4,5,6,name="liu",age=18)    #注意：添加字典时key和value用等号连接
