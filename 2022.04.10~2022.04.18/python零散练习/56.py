#完整for循环语法
for num in [1,2,3,4,5]:
    print(num)
    if num == 2:
        break
else:#如果前面使用了break，else将不会被执行
    print("会执行吗")
print("循环结束")

