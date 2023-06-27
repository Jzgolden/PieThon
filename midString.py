def mid(string):
    length = len(string)
    if length % 2 == 0:
        return ""
    else:
        middle_index = length // 2
        return string[middle_index]

# Testing the function
print(mid("abc"))   # Output: "b"
print(mid("aaaa"))  # Output: ""