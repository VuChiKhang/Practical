print ("            Menus ")
print ("  No.  |   Product   |   Price")
print ("   1   |   Burger    |    $6.6")
print ("   2   |   Fries     |    $3.4")
print ("   3   |   Coke      |    $2.3")
print ("   4   |   Pizza     |    $12.5")

choice = float(input("Which product do you choose? Please enter the product number: "))

while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
    print("Error!")
    choice = float(input("Which product do you choose? Please enter the product number: "))

num = float(input("How many do you order: "))
total=0.0
if choice == 1:
    price =6.6
elif choice == 2:
    price =3.4
elif choice == 3:
    price =2.3
elif choice == 4:
    price =12.5

total1=price * num

print ()
print ("            Menus ")
print ("  No.  |   Product   |   Price")
print ("   1   |   Burger    |    $6.6")
print ("   2   |   Fries     |    $3.4")
print ("   3   |   Coke      |    $2.3")
print ("   4   |   Pizza     |    $12.5")

choice = float(input("Which product do you choose? Please enter the product number: "))
num = float(input("How many do you order: "))
total=0.0
if choice == 1:
    price =6.6
elif choice == 2:
    price =3.4
elif choice == 3:
    price =2.3
elif choice == 4:
    price =12.5
total2=price * num
total =total1 + total2
print ("The Final Total price: $",total)