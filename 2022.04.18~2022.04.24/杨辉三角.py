#杨辉三角
n = int(input("请输入n的值："))
ayanghuisanjiao = [[1] * i for i in range(1, n + 1)]
#print(ayanghuisanjiao)
for i in range(len(ayanghuisanjiao)):
    for j in range(len(ayanghuisanjiao[i])):
        #print(ayanghuisanjiao[i][j])
        if j != 0 and j != len(ayanghuisanjiao[i]) - 1:
            ayanghuisanjiao[i][j] = ayanghuisanjiao[i - 1][j - 1] + ayanghuisanjiao[i - 1][j]
    print(" ".join(map(lambda x: str(x), ayanghuisanjiao[i])))1