
class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")

#创建对象
tom = Cat()

tom.drink()
tom.eat()

#再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

#tom和lazy_cat不是同一只猫
