print("Profit & Loss Calculator")

flag = True
while flag:
    costPrice = float(input("What is the Cost Price of the Product?\n₹"))
    sellingPrice = float(input("What is the Selling Price of the Product?\n₹"))

    if costPrice == sellingPrice:
        print("Cost Price and Selling Price are same Hence\n there is no loss or profit")
    elif costPrice > sellingPrice:
        print(f'There is Loss of ₹{costPrice - sellingPrice}')
    elif sellingPrice > costPrice:
        print(f'There is Profit of ₹{sellingPrice - costPrice}')

    opp = input("Press N to check another Press E to exit: ")
    if opp == "E":
        flag = False
