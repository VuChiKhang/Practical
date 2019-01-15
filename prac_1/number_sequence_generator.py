
x = int(input("Enter start number: "))
y = int(input("Enter stop number: "))
while (x<0 or y<0):
    print ("Error! Please enter again! >>> ")
    x = int(input("Enter start number: "))
    y = int(input("Enter stop number: "))

l = range(x,y)
result=[]
for i in l:
    if i % 2 ==0:
        result.append(i)
print ("Result for even number from x to y: ",result)

result2=[]
for i in l:
    if i % 2 !=0:
        result2.append(i)
print ("Result for odd number from x to y: ",result2)

result3=[]
for i in l:
    if i >= 0:
        i=i*i
        result3.append(i)
print ("Result for square number from x to y: ",result3)