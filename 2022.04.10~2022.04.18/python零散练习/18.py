#牛顿环实验计算
Dm = float(input("请输入Dm："))/1000
Dn = float(input("请输入Dn："))/1000
m = float(input("请输入M："))
n = float(input("请输入N："))
a = 5.7E-7
R = (Dm**2-Dn**2)/(4*(m-n)*a)
print("R的值为：",R)