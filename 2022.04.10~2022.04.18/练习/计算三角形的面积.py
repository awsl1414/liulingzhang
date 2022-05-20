a = int(input("输入三角形第一边长:"))
b = int(input("输入三角形第二边长:"))
c = int(input("输入三角形第三边长:"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))
print("此三角形面积为：%d"%area)