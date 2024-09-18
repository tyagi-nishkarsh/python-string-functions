#27. Write a Python program to find the most frequent word in a string and its frequency


a = input("Enter a sentence : ")
a = a.lower()
wordss = a.split()
words = [''.join(i for i in word if i.isalnum()) for word in wordss]

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

most_frequent_word = ""
t_count = 0

for word, count in freq.items():
        if count > t_count:
            most_frequent_word = word
            t_count = count

print(f"The most frequent word is '{most_frequent_word}' with a frequency of {t_count}.")
