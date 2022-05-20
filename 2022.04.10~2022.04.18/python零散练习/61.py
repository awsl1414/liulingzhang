
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
a = power(5)
print(a)
# x = 5
# n = 3
# s = 1
# while n > 0:
#     n = n - 1
#     s = s * x
# print(s)
# def power(x,n):
#     s = 1
#     while n > 0:
#         n -= n
#         s = s*x