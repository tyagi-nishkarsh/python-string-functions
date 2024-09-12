#29. Write a Python program to remove all special characters from a string except alphabets and numbers

a = input("Enter a string: ")

b = ''.join(letter for letter in a if letter.isalnum())

print(b)
