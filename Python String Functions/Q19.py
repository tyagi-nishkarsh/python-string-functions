#19. Write a Python program to find the most frequent character in a string.

a = str(input("Enter a string: "))

freq = {}

for char in a:
	if char in freq:
		freq[char] += 1
	else:
		freq[char] = 1

most_frequent_char = None
max_count = 0

for char, count in freq.items():
    if count > max_count:
        max_count = count
        most_frequent_char = char

print("The most frequent character is  : " + str(most_frequent_char))
