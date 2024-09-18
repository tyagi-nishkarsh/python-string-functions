#21. Write a Python program to check if a string is a palindrome.

a = input("Enter a string: ")
d = a.replace(" ", "")

if d.isalnum():
        b = d.lower()

print(b)
if b == b[::-1]:
        print(f"The string '{a}' is a palindrome.")
else:
        print(f"The string '{a}' is not a palindrome.")

