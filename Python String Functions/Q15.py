#15 Write a Python program to find the position of the last occurrence of a substring in a string

a = str(input("Enter a string: "))
b = str(input("Enter the substring: "))
c =(a.rfind(b))
if c == -1:
    print(f"The substring '{b}' is not found in the main string.")
else:
    print(f"The last occurrence of the substring '{b}' is at index {c}.")
