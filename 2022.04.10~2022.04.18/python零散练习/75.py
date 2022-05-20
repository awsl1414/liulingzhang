#递归
def sum_numbers(num):
    print(num)
    if num == 1:    #递归的出口，不指定容易造成死循环
        return
    sum_numbers(num-1)
sum_numbers(3)
#特点：自己调用自己
#注意：一定要留出递归的出口，否则容易出现死循环
