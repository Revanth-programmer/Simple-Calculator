print("Welcome to the calculator by REV studios")
print("Please Enter which Mathemetical operation do you want to perform ?")
a = input()
b = int(input("Please Enter the first number"))
c = int(input("Please Enter the second number"))
if a == '+' :
    print(b+c)
if a == '-' :
    print(b-c)
if a == '*' :
    print(b*c)
if a == '/' :
    print(b/c)