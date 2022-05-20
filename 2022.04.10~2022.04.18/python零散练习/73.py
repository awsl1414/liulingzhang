def sum_numbers(*args): 
    num = 0
    for a in args:
        num += a
    print(args)
    return num
result = sum_numbers(1,2,3,4,5,6,7,8)
print(result)
