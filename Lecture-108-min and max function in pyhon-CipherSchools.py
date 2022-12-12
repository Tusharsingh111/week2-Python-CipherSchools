# max and min function in python
numbers = [1,4,5,14,60]
print(min(numbers))
print(max(numbers))

def greatest_diff(l):
    return max(l)-min(l)
print(greatest_diff(numbers))