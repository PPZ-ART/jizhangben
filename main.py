支出记录=[]
while True:
    print("========= 记账本 =========")
    print("1. 加一笔支出")
    print("2. 查看所有明细")   
    print("3. 查看总支出")
    print("4. 查看记账笔数")
    print("5.删除最后一笔支出")
    print("6. 退出")
   
    选择 = input("请选择操作（1/2/3/4/5/6）：")
    if 选择=="1":
        金额=float(input("请输入金额："))
        支出记录.append(金额)
        print("已计入",金额,"元")

    elif 选择=="2":
        print("明细如下：")
        for 金额 in 支出记录:
            print(" -",金额,"元")   

    elif 选择=="3":
        print("总支出为：",sum(支出记录),"元")

    elif 选择=="4":
        print("总记账笔数为：",len(支出记录),"笔")

    elif 选择=="5":
        if 支出记录:
            print("已删除",支出记录.pop(),"元")
        else:
            print("没有可删除的支出记录")

    elif 选择=="6":
        print("已退出，天天开心")
        break 
    else:
        print("无效的选择，请重新输入1/2/3/4/5/6")