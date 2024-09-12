#30. Write a rython program to hind the smallest and largest character in a string

a = input("Enter a string: ")

b = [n for n in a.split() if len(n) == max([len(k) for k in a.split()])]
c = [n for n in a.split() if len(n) == min([len(k) for k in a.split()])]

print(f"The smallest character is '{c}' and the largest character is '{b}'")


