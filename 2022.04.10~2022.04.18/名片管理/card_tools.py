#记录所有名片列表
card_list = []
def show_menu():
    #显示菜单
    print("*"*50)
    print("")
    print("欢迎使用【名片管理系统】0.1  by c405小刘\n1.新增名片\n2.显示全部\n3.查询名片")
    print("")
    print("0.退出系统")
    print("*"*50)
def new_card():
    #新增名片
    print("-"*50)
    print("新增名片")
    #1.提示用户输入名片信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ:")
    email = input("请输入邮箱：")
    #2.使用用户名输入的信息建立一个名片字典
    card_dict ={"name":name,
                "phone":phone,
                "qq":qq,
                "email":email}
    #3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    #4.提示用户添加成功
    print("添加%s的名片成功"%name)
def show_all():
    #显示所有名片
    print("-"*50)
    print("显示所有名片")
    #判断是否存在名片记录，如果没有，提示用户返回
    if len(card_list) == 0:
        print("当前没用任何名片记录，请使用新增功能添加名片")
        return#如果return后面没有任内容，表示会返回到调用函数的位置，并且不会返回任何结果
    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")
    #打印分隔线
    print("="*50)
    #遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
def search_card():
    #查询名片
    print("-"*50)
    print("查询名片")
    #1.提示用户输入要搜索的姓名
    find_name = input("请输入你要搜索的姓名：")
    #2.遍历名片列表，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("*"*50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t"%(card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
        #针对找到的名片记录执行修改和删除的操作
        deal_card(card_dict)
        break
    else:
        print("抱歉，没有找到%s"%find_name)
def deal_card(find_dict):
    action_str = input("请输入对名片的操作：[1].修改 [2].删除 [0].返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ:")
        find_dict["email"] = input_card_info(find_dict["email"],"邮箱：")
        print("修改名片成功！")
    elif action_str == "2":
        print("删除名片")
        card_list.remove(find_dict)
        print("删除名片成功！")
def input_card_info(dict_value,tip_message):
    #1.提示用户输入内容
    result_str = input(tip_message)
    #2.针对用户的输入进行判断，如果用户输入了内容，返回内容
    if len(result_str) > 0:
        return result_str
    #3.如果用户没有输入，返回字典中原有的值
    else:
        return dict_value