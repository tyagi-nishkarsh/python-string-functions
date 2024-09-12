#27. Write a Python program to find the most frequent word in a string and its frequency


a = input("Enter a string: ")
a = a.lower()
words = a.split()
for char in ",.?!;:":
        a = a.replace(char, ' ')

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = None
most_frequent_count = 0

for word, count in word_count.items():
        if count > most_frequent_count:
            most_frequent_word = word
            most_frequent_count = count

print(f"The most frequent word is '{most_frequent_word}' with a frequency of {most_frequent_count}.")
