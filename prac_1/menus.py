name = str(input("Enter name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = str(input("Get choice: "))
while (choice != 'H' and choice != 'G' and choice != 'h' and choice != 'g' and choice == 'Q' and choice == 'q'):
    print ("Invalid choice")
    choice = str(input("Get choice: "))

while choice == 'H' or choice == 'h' or choice =='G' or choice == 'g':
    if choice != 'Q'or choice != 'q':
     if choice == 'H' or choice == 'h':
        print ("Hello",name)

     elif choice == 'G'or choice == 'g':
        print ("Goodbye",name)

     choice = str(input("Get choice: "))
if choice == 'Q' or choice == 'q':
    print ("Finished!")