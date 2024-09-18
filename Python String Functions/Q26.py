#26. Write a Python program to extract all numbers from a string and return them as a list

a = input("enter a string: ")
l = []
num=["0","1","2","3","4","5","6","7","8","9","0"]
for i in range(len(a)):
    if a[i] in num:
        l.append(a[i])
print(l)