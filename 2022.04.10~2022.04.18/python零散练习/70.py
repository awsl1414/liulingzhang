#缺省参数(定义默认参数)
#注意事项：
#1.必须保证带有默认值的缺省参数在参数列表末尾
#2.在调用函数时，如果有多个缺省参数，需要指定参名，这样解释器才能够知道参数的对应关系
def print_info(name,gender=True):       #在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s"%(name,gender_text))
print_info("小明")
print_info("小美",False)