def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrom("madam"))
print(is_palindrom("Nishant"))
print(is_palindrom("kanak"))


def is_palindrom(word):
    if word == word[::-1]:
        return True
    return False

print(is_palindrom("madam"))
print(is_palindrom("Nishant"))
print(is_palindrom("kanak"))
