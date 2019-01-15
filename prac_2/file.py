out_file=open("data.txt",'w')
name = input("What is your name: ")
print(name, file = out_file)
out_file.close()

in_file=open("data.txt",'r')
name = in_file.read().strip()
print("Your name is ",name)
in_file.close()