#29. Write a Python program to remove all special characters from a string except alphabets and numbers

a = input("Enter a string: ")
b = ''.join(char for char in a if char.isalnum())


print(b)

