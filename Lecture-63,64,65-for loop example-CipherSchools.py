#lecture-63
# sum from 1 to n
n=int(input("enter a number: "))
total = 0
for i in range (1,n+1):
    total+=i
print(total)


#lecture-64
#calculate sum of digits ----> 1 + 2 + 5 + 6
total = 0
num = input("enter a number : ")
for i in range(0, len(num)):
    total += int(num[i])

print(total)

#lecture-65
name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:  {name.count(name[i])}")
        temp +=name[i]