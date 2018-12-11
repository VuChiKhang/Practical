num=int(input("Enter number if items"))
while(num<=0) :
    print("Enter a positive number")
total=0.0
for i in range (0,num):
    price=float(input("enter price of item"))
    total+=price
    print("price=",price,"total=",total)

    if (total>=100):
        total= 0.9*total
        print ("total price of item is",total)