import time
Bottles=int(input("Enter number of bottles:"))
while Bottles != 0:
    print((str(Bottles)+" green bottles, hanging on the wall"))
    print((str(Bottles)+" green bottles, hanging on the wall"))
    print("And if 1 green bottle should acidentally fall,")
    Bottles=Bottles-1
    time.sleep(2)
print()
print("There will be no green bottles, hanging on the wall.")
