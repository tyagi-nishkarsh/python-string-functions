#4 Write a Python program to check if a string ends with a specific suffix.

a = str(input("Enter a string: "))
b = str(input("Enter the suffix : "))
if a.endswith(b):
    print(f"The string '{a}' ends with the suffix '{b}'.")
else:
    print(f"The string '{a}' does not ends with the suffix '{b}'.")