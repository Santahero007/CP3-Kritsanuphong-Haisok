menuList = []
priceList = []

def showBill():
    print("----Food List----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("Total",str(sum(priceList)),"THB")
while True:
    menuName = input("Price Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()





