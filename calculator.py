x=int(input("Enter the value 1: "))
y=int(input("Enter the value 2: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice: "))
if choice==1:
    print(x+y)
elif choice==2:
    print(x-y)
elif choice==3:
    print(x*y)
elif choice==4:
    print(x/y)  
else:
    print("Incorrect choice")
