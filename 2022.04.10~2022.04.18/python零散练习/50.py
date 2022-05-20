#文字对齐方式/
pome = ["登鹳雀楼",
        "王之涣",
        "白日依山尽，",
        "黄河入海流。",
        "欲穷千里目，",
        "更上一层楼。"]
print(pome)
for a in pome:
    print("|%s|"%a.center(10))
for b in pome:
    print("|%s|"%b.center(10,"　"))
for c in pome:
    print("|%s|"%c.rjust(10,"　"))

