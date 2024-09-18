#20. Write a Python program to remove all vowels from a string.

vowels = 'aeiouAEIOU'

a = input("Enter a string: ")

s = ""
for char in a:
    if char not in vowels:
        s += char

print(s)



