#25. Write a Python program to find the longest substring without repeating characters in a string

s = "nandu"  # input string
max_len = 0
max_substr = ""
start = 0
char_index = {}

for end, char in enumerate(s):
    if char in char_index and char_index[char] >= start:
        start = char_index[char] + 1
    char_index[char] = end
    if end - start + 1 > max_len:
        max_len = end - start + 1
        max_substr = s[start:end+1]

print("Longest substring without repeating characters:", max_substr)

