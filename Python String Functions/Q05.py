#5. Write a Python program to find the first occurrence of a substring in a string.

a = str(input("Enter a string: "))
b = str(input("Enter the substring: "))
c =(a.find(b))
if c != -1:
    print(f"The first occurrence of '{b}' is at index {c}.")
else:
    print(f"The substring '{b}' was not found in the string.")