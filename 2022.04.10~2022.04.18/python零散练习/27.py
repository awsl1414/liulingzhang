a = 0
sum = 0
while a <= 10:
    sum += a
    a = a + 1
    if a == 5:
        a += 1
        continue
print(sum)