sum = 0
a = 0
while a <= 100:
    if a % 2 == 0:
        sum += a
        if a == 98:  
            break   #break通常与if连用
    a += 1
print(sum)