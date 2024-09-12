#3. Write a Python program to check if a string starts with a specific prefix.

a = str(input("Enter a string: "))
b = str(input("Enter the prefix : "))
if a.startswith(b):
    print(f"The string '{a}' starts with the prefix '{b}'.")
else:
    print(f"The string '{a}' does not start with the prefix '{b}'.")