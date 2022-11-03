try:
    while(True):
        menu=["Espresso","Cappucino","Latte"]
        hotorcolde=["hot","colde"]
        price=[55,60]
        def  wrong():
            print("Sorry, something went wrong\n")
        def _type(hotcolde,menunum,pricenum):
            print("---You chose %s %s %d baht---\n"%(hotorcolde[hotcolde],menu[menunum],price[pricenum]))  
        def selcettype(coffee,selcet_type):
            if coffee == "1":
                if selcet_type == "1":
                    _type(0,0,0)
                elif selcet_type == "2":
                    _type(1,0,1)
            elif coffee == "2":
                if selcet_type == "1":
                    _type(0,1,0)
                elif selcet_type == "2":
                    _type(1,1,1)
            elif coffee == "3":
                if selcet_type == "1":
                    _type(0,2,0)
                elif selcet_type == "2":
                    _type(1,2,1)
        def formoney(yourmoney,selcet_type):
                if selcet_type=="1":
                    _price=price[0]
                if selcet_type=="2":
                    _price=price[1]
                if yourmoney>=_price:
                    print("You recieved a change of %.2f baht\n---Thank you---"%(yourmoney-_price))
                if yourmoney<_price:
                    print("Not enough money\n---Please try again---")  
                        
        print("---Welcome to Tokyo Rebvengers's Coffee---\n")
        show_menu=input("Please type 1 to show menu :\t")
        if show_menu=="1":
            print("\n---choose the menu---\n1.\t%s\n2.\t%s\n3.\t%s\n"%(menu[0],menu[1],menu[2]))
        else:
            wrong()
            break
        coffee=input("Select coffee :\t")
        if not coffee == "1" and not coffee == "2" and not coffee == "3":
            wrong()
            break
        print("\n---Choose the type of the coffee---\n1.\tHot %d baht\n2.\tColde %d baht\n"%(price[0],price[1]))
        selcet_type =input("Select type :\t")
        if not selcet_type == "1" and not selcet_type == "2":
            wrong()
            break
        selcettype(coffee,selcet_type)
        inputmoney=int(input("Input your money :\t"))
        formoney(inputmoney,selcet_type)

except Exception as message:
    print(message)