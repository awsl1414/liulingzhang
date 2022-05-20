#递归实现数字累加
def sum_numbers(num):
    #出口
    if num == 1:
        return 1
    temp = sum_numbers(num-1)
    return num + temp
a = sum_numbers(500)
print(a)