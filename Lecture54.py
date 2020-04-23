def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- WeShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate():
    totalPrice = int(input("Enter your price :"))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Include vat", result, "THB")
def vatInclude(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print("Total :", vatInclude(price1 + price2), "THB")


if login():
    showMenu()
    menu = menuSelect()
    if menu == 1:
        vatCalculate()
    elif menu == 2:
        priceCalculate()
    else:
        print("Error!!!")
else:
    print("Invalid ID!")

print("End the Program")







