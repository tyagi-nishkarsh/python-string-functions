#25. Write a Python program to find the longest substring without repeating characters in a string

a = input("enter a string: ")
x = ""
y = ""

for char in a:
    if char not in y:
        y += char
        if len(y) > len(x):
            x = y
    else:
        y = y[y.index(char) + 1:] + char

print("The longest substring without repeating characters is:", x)
