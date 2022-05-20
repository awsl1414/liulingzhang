def triangle(n):
    l=[] #用来存储所有行的返回列表
    for i in range(n):
        if i==0:
            l.append([1])  # 第一行
        elif i==1:
            l.append([1,1])#第二行
        #第三行以后.....
        else:
            y = []  # 存储一行，每次清空
            for j  in range(i+1):
                if j==0 or j==i:
                    y.append(1)#行首和行末为1
                else:
                    y.append(l[i-1][j]+l[i-1][j-1])
            l.append(y)#放入所有行存储列表中
    return l
n= int(input("请输入n：")) #行数12
x=triangle(n)
for i in range(len(x)):#逐行打印结果
    print(x[i])