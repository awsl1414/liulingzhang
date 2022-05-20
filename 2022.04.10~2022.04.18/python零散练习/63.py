def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
# 把大象装冰箱一共分三步：
# 第一步把'A'上面的'n-1'个盘子移动到'B'上面
# 第二步把'A'最下的' 1 '个盘子移动到'C'上面
# 第三步把'B'所有的'n-1'个盘子移动到'C'上面
print(move(4,"a","b","c"))