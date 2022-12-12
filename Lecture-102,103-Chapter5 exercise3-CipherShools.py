def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words = ['abc', 'tuv', 'xyz']
print(reverse_elements(words))