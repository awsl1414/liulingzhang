#给对象增加属性
#在python中，要给对象设置属性很简单，但不推荐使用
#原因：对象属性的封装应在类的内部

#语法：对象+.属性名+赋值语句

class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")

#创建对象
tom = Cat()

tom.name = "tom"
tom.drink()
tom.eat()

#再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()