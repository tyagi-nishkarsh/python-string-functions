#9 Write a Python program to split a string by spaces and join it back using a hyphen.

a = input("Enter the string: ")
b = a.split()
c = '-'.join(b)
print(c)