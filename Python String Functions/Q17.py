#17 Write a Python program to find all the words in a string that are longer than a specified length.

a = input("Enter a string: ")
b = int(input("Enter the specified length: "))

list = []
text = a.split(" ")
for x in text:
	if len(x) > b:
		list.append(x)
print(f"The words that contain more than {b} letters are {list}")