#
# in_file = open("numbers.txt",'r')
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# result=number1+number2
# print("The result is: ",result)
# in_file.close()

in_file = open("numbers.txt",'r')
total=0
for line in in_file:
    number = int(line)
    total+=number
print(total)