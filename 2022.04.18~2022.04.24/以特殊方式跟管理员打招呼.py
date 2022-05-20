gl_administrators = ["Admin","Tom","Shuishou","Lucy","Ben"]
for administrator in gl_administrators:
    if "admin" == administrator:
        print("Hello Admin, would you like to see a status report?")
    elif "Tom" == administrator:
        a = "Tom"
        print(a)
    elif "Shuishou" == administrator:
        a = "Shuishou"
    elif "Lucy" == administrator:
        a = "Lucy"
    elif "Ben" == administrator:
        a = "Ben"
    print("Hello "+ str(a) +", thank you for logging in again")
# print(gl_administrators)
# a = 1
# b = 2
# sum = a + b
# print("%d+%d=%d"%(a,b,sum))