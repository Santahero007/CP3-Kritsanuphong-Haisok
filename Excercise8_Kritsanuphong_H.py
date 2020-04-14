userInput = input("Username :")
passwordInput = input("Password:")
if userInput == "redsun" and passwordInput == "888" :
    print("{----Welcome to Redsun Restaurant----}")
    print("{---Please Seclect Your Menu---}")
    print("{--- GOHAN MONO---}")
    print("1.Tekka-Don(ข้าวหน้าปลาโอญี่ปุ่น) x 1    500 THB")
    print("2.Katsu-Don(ข้าวหน้าหมูทอด)    x 1    200 THB")
    print("3.Ten-Don(ข้าวหน้าเทมปุระ)      x 1    220 THB")
    print("{--- SUSHI ---}")
    print("4.Akami(ข้าวปั้นหน้าปลาโอญี่ปุ่น)    x 1   280 THB")
    print("5.Ikura(ข้าวปั้นหน้าไข่ปลาแซลมอน) x 1   220 THB")
    print("6.Hamachi(ข้าวปั้นหน้าปลาฮามาจิ)   x 1   280 THB")
    print("{--- SALAD ---}")
    print("7.Chashu-Salad(สลัดหมูชาชู)     x 1   180 THB")
    print("8.Caesar-Salad(ซีซ่าร์สลัด)      x 1   240 THB")
    print("9.Tuna-Salad(สลัดทูน่า)         x 1   180 THB")

    print("Choose Your MenuNumber {1-9}")
    menuNumber = input(">>")
    print("How many ?")
    many = int(input(">>"))
    vat = 7

    if menuNumber == "1":
        result1 = (500 * many + (500 * vat / 100))
        print("Total = ",result1,"THB")
    if menuNumber == "2":
        result2 = (200 * many + (200 * vat / 100))
        print("Total = ", result2, "THB")
    if menuNumber == "3":
        result3 = (220 * many + (220 * vat / 100))
        print("Total = ", result3, "THB")
    if menuNumber == "4":
        result4 = (280 * many + (280 * vat / 100))
        print("Total = ", result4, "THB")
    if menuNumber == "5":
        result5 = (220 * many + (220 * vat / 100))
        print("Total = ", result5, "THB")
    if menuNumber == "6":
        result6 = (280 * many + (280 * vat / 100))
        print("Total = ", result6, "THB")
    if menuNumber == "7":
        result7 = (180 * many + (180 * vat / 100))
        print("Total = ", result7, "THB")
    if menuNumber == "8":
        result8 = (240 * many + (240 * vat / 100))
        print("Total = ", result8, "THB")
    if menuNumber == "9":
        result9 = (180 * many + (180 * vat / 100))
        print("Total = ", result9, "THB")

    print("> Thank You to Visit Our Restaurant <")

else:
    print("- {Invalid Id !!} -")
    print("- {Please Try Agian !!} -")













