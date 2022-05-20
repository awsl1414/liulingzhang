#第一个面向对象程序
#需求：小猫爱吃鱼，小猫要喝水

#定义类
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")

#创建对象
tom = Cat()

tom.drink()
tom.eat()

print(tom)
addr = id(tom)
print("%d"%addr)
print("%x"%addr)