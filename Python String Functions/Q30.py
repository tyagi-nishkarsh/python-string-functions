#30. Write a rython program to find the smallest and largest character in a string

a = input("Enter a string: ")
smallest_char = a[0]
largest_char = a[0]

for char in a:
    if char < smallest_char:
        smallest_char = char
    elif char > largest_char:
        largest_char = char

print("Smallest character:", smallest_char)
print("Largest character:", largest_char)



