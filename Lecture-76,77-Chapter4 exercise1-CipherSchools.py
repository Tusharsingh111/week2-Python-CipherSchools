def greater(a,b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
bigger = greater(num1,num2)

print(f"{bigger} is grater")