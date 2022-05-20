sum = 0
a = 0
while a <= 100:
    a += 1
    if a % 2 == 0:
        sum += a
        if a == 98:
            a += 1
            continue    #注意先修改条件数值，不然会进入死循环
    print(sum)