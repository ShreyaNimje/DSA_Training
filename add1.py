# age =33
# name = "Shreya"
# pi = 3.14
# result = True
# print(type(age))
# print(type(name))
# print(type(pi))
# print(type(result))

# age =33
# name = "Shreya"
# pi = 3.14
# result = True
# print(id(age))
# print(id(name))
# print(id(pi))
# print(id(result))

#why all fundamentals datatypes are immutable
# math = 50 
# chem = 50 
# phy = 50
# print(id(math)) 
# print(id(chem))
# print(id(phy))

# #Simple if

# 5

# print(2+2)
# print("2" + "2")
# a= int (input("Emter first number:"))
# b= int (input("Emter Second number:"))
# print(a+b)

# Types of values that can be typecasted with integer typecast
# print(int(3.14))
# #print(int(10 + 5j)) # Cannot typecast Complex numbers
# print(int(True))
# print(int(False))
# #print(int("3.14")) # Cannot type cast Float stored as string
# print(int("4"))

# Types of values that can be typecasted with float typecast
# print(float(3.14))
# #print(float(10 + 5j)) # Cannot typecast Complex numbers
# print(float(True))
# print(float(False))
# print(float("3.14")) # Cannot type cast Float stored as string
# print(float("4"))
# print(float(3.14))

# # Types of values that can be typecasted with complex typecast
# print(complex(3.14))
# print(complex(True))
# print(complex(False))
# print(complex("3.14")) # Cannot type cast Float stored as string
# print(complex("4"))
# print(complex(3.14))
# #print(complex("name"))
# print(complex(True, False))
# print(complex(5, -3))

# # Types of values that can be typecasted with bool typecast
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))
# print(bool("shreya"))
# # Bool typecast converts values with 0 or only with 0 to false and all other are converted to true


#simple if
# a= int (input("Enter any single digit : "))
# if a>0:
#     print("Positive Number")
# if a<0:
#     print("Negative Number")
# if a == 0:
#     print("zero")

#simple if else
# a= (input("Enter any day : "))
# if a=[M,T,W,F]:
#     print("It is a working day")
# else :
#     print("It is weekend")

# day = input("Enter your day name :")
# if day == "saturday" or day == "SATURDAY" or day == "SUNDAY" or day == "sunday" :
#     print("weekend")
# else:
#     print("working day")

# per = 65
# if per >= 65:
#     print("grade A")
# elif per <= 65 and per >= 50:
#     print("grade B")
# else:
#     print("Fail")

# a=ord(input("Enter Something:"))
# if a>=65 and a<=90:
#     print("This is UpperCas")
# elif a>97 and chr <=122:    
#     print("This is Lower Case")
# elif a>48  and a<=57 :
#     print("This is digit")
# else:
#     print("Special Symbol")

#Membership operator
# name = "help4code"
# print('h' in name)
# print('h' not in name)

# #identity operator for address comarison
# math = 50
# chem = 50
# print(math is chem)

#For Loop
# for i in range(5):#i = 0
#     print(i)
# for i in range(2,10):
#     print(i)
# for i in range(2,11,2):
#     print(i)
# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j)
#     print(".................")

# for i in range(1,11):
#     print(i*2, " ", i*3, " ", i*4, " ", i*5)
# print("___________")
# for i in range(1,11):
#     print(i*11," ", i*12," ", i*13," ", i*14)

#--------------------------Task------------------------------#
# a=int(input("Enter the Marks of Paper 1:"))
# b=int(input("Enter the Marks of Paper 2: "))
# c=int(input("Enter the Marks of Paper 3: "))
# total = a + b + c
# per = (total / 3.0)

# print("Total =",total)
# print("Percentage =",per)
# if a>45 and b>45 and c>45:
#     print("Pass")
# else:
#     print("Fail")

# gender = input("Enter your gender(M/F): ")
# if per >= 65 and gender == "M":
#     print("Eligible for placement")
# else:
#     print("Not eligible")

#------------------------Q---------------------------------#
for i,j in zip(range(1,6), range(5,0,-1)):
    if i == 3 and j == 3:
        continue
    print(i, "  ", j)