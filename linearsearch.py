# def linearSearch(array, target):
#     for i in range(0, len(array)):
#         if array[i] == target:
#             return i
#     return -1

# array = [1,2,3,4,8,9,7]
# target = 8
# result = linearSearch(array, target)
# if result == -1:
#     print("Target value not found")
# else:
#     print("Element found at index ", i)

#removing spaces from string:
# 1. rstrip ==> To remove spaces at right hand side
# 2. lstrip ==> To remove spaces at left hand side
# 3. strip ==> To remove spaces both side
# city = input("Enter your city name: ")
# scity = city.strip()
# if scity == 'Hyderabad' :
#     print("Hello hyderabadi...")
# elif scity == 'Chennai' :
#     print("Hello madrasi...")
# elif scity == "Banglore":
#     print("Hello Kannadiga....")
# else: 
#     print("your entered city is invalid")

# r = [[100, 198, 333, 323],
#       [122, 232, 221, 111],
#       [223, 565, 245, 764]]
# r1 = r[0]
# for i in range(len(r1)):
#     max = r1[0]
#     if max < r1[i]:
#         max = r1[i]
# print("Max of row 1 :", max)
# r2 = r[0]
# for i in range(len(r2)):
#     max1 = r2[0]
#     if max1 < r2[i]:
#         max1 = r2[i]
# print("Max of row 2 :", max1)
# r3 = r[0]
# for i in range(len(r3)):
#     max2 = r3[0]
#     if max2 < r3[i]:
#         max2 = r3[i]
# print("Max of row 3 :", max2)
r = [[100, 198, 333, 323],
     [122, 232, 221, 111],
     [223, 565, 245, 764]]
# Row 1
# r1 = r[0]
# max1 = r1[0]
# for i in range(len(r1)):
#     if max1 < r1[i]:
#         max1 = r1[i]
# print("Max of row 1 :", max1)
# # Row 2
# r2 = r[1]
# max2 = r2[0]
# for i in range(len(r2)):
#     if max2 < r2[i]:
#         max2 = r2[i]
# print("Max of row 2 :", max2)
# # Row 3
# r3 = r[2]
# max3 = r3[0]
# for i in range(len(r3)):
#     if max3 < r3[i]:
#         max3 = r3[i]
# print("Max of row 3 :", max3)

#input = Prashant*is*a*good*Programmer
# a = input("Enter input string :")
# b = ''
# v = ''
# for i in a:
#     if i != '*':
#         b += i
#     else:
#         v += i
# print(b)
# print(str(v+b))

#i/p = aaabbbbccceeeee
#o/p = a3b4c3d5
a = "aaabbbbccceeeee"
b = {}
for i in range(len(a)):
    key = a[i]
    count = 0
    for j in range(len(a)):
        if key == a[j]:
            count+=1
        b[key] = count
#print (b)
for i, j in b.items():
    print(i, j, sep='', end='')