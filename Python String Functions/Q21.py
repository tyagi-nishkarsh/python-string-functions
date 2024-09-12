#21. Write a Python program to check if a string is a palindrome.

a = input("Enter a string: ")

b = ''.join(char.lower() for char in a if char.isalnum())
if b == b[::-1]:
        print(f"The string '{a}' is a palindrome.")
else:
        print(f"The string '{a}' is not a palindrome.")