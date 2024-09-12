#18. Write a Python program to convert a string to a list of characters and back to a string.

a = input("Enter a string: ")
b = list(a)
print(f"List of characters: {b}")


c = "".join(b)
print(f"string: {c}")

