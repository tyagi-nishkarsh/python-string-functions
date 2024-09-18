#28. Write a Python program to check if two strings are anagrams

a = input("Enter the first string: ")
b = input("Enter the second string: ")

a = a.lower()
b = b.lower()

if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
