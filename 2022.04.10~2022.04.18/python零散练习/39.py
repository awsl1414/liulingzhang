from unicodedata import name


num_list = ["2","3","1","5","4"]

#升序
num_list.sort()
print(num_list)
#降序
num_list.sort(reverse=True)
print(num_list)
#逆序(反转)
num_list.reverse()
print(num_list)