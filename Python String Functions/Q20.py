#20. Write a Python program to remove all vowels from a string.

vowels = 'aeiouAEIOU'

a = input("Enter a string: ")
b = ''.join(char for char in a if char not in vowels)
print(f"String after removing vowels: '{b}'")


