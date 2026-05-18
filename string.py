# name = "shreyanimje"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[10])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# s = "Python is High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# name = "Shreya"
# sal = 5000
# age = 28
# print("{} sal is {} age is {}". format(name, sal, age))
# print("{0} sal is {1} age is {2}". format(name, sal, age))
# print("{x} sal is {y} age is {z}". format(x=name,y = sal, z=age))
# A=1
# print(f"{A} is a good boy")

# name = "shreya"
# for i in name:
#     print(i)

# name = "prashant"
# A = ""
# for i in (name[::-1]):
#     if i not in A:
#         A = A + i
# print(A)
# print(A[::-1])

# N = len(name)
# for i in range(N-1, -1,-1):
#     A += name[i]
# print(A)

# W = "racecar"
# W = "berry"
# A = ""
# N = len(W)
# for i in range(N-1, -1,-1):
#     A += W[i]
# if A == W:
#     print("String is Plalindrome")
# else:
#     print("Not a palindrome")
# print(A)
# print(W)
#Annagram
# word = "listen"
# word1 ="silent"
# if len(word) == len(word1):
#     print("count of word = count of word1")

# vowels = ['a','e','i','o','u']
# name = "hello"
# cons = 0
# vow = 0
# for i in name:
#     if i in vowels:
#         vow += 1
#     else:
#         cons += 1
# print(cons)
# print(vow)

# sent = "This is a String"
# count = 0
# for i in sent:
#     if i ==" ":
#         count += 1
# if count > 0:
#     count += 1
# print(count)

# 'a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print'

# spe = ['@', '#', '!','$','%','.','^','*']
# name = input("Enter the string: ")
# s = 0
# w = 0
# for i in name:
#     if i in spe:
#         s += 1
#     if i == " ":
#         w += 1
# print("Count =", s + w)

# st = input("Enter the string to convert into title format:")
# print(st.title())

# print('shreyanimje2'.isalnum())
# print('Shreyanimje'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Shreya'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

print("Shreya".find("y"))
print("Shreya".index("r"))
print("Shreya Nimje".count("e"))
