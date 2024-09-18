#23. Write a Python program to find the longest word in a string.


a = input("Enter a string: ")
b = a.split()
longest_word = ''
for i in b:
        if len(x) > len(longest_word):
            longest_word = x

print(f"The longest word in the string is: '{longest_word}'")