 # scope
x = 5

def fun():
    global x
    x = 7   #local variables
    return x

print(x)
print(fun())
print(x)
