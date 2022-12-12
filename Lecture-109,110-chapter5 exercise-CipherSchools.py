def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

mixed = [1,2,3, [1,2],[3,4]]
print(sublist_counter(mixed))

mixed = [1,2,3, [1,2]]
print(sublist_counter(mixed))

mixed = [1,2,3]
print(sublist_counter(mixed))