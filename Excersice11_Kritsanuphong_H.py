numberInput = int(input("How tall your Pyramid is? :"))

for x in range (numberInput):
    print(" " * (numberInput-(x-1)) + "*"*(x*2+1))