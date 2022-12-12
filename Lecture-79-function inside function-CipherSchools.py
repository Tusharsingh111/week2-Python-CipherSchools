#function

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


# function in function

def new_greatest(a,b,c):
    bigger = greatest(a,b)
    return greatest(bigger, c)

print(new_greatest(10,20,30))

