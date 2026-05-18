# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(chr(64+i),end=" ")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+j),end=" ")
#     print()

# import time
# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(" "*(n-i), end=" ")
#     for j in range(1, i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()

# n = [1, 2, 3, 4]
# l = []
# for i in n:
#     l[i] = n[i+1]*n[i+2]*n[i+3]
#     print(l)

#Maximum Consecutive ones
# Arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
# count = 0
# max_count = 0
# for i in Arr:
#     if i == 1:
#         count += 1
#         max_count = max(max_count, count)
#     else:
#         count = 0
# print(max_count)

str = input("Insert the String to check substring :")
sta = input("Insert the substring to be checked :")
count = 0
for (i and i + 1) in str:
    if i == sta:
        count += 1
    else:
        count = 0
print(count)