# i = 1
# while i<= 5:
#     print(i)
#     i += 1

#function
# def hello(): #called function
#     print("Hello World")
# hello() # calling function
# hello()

# def arithematic():
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# print(arithematic())
# result = arithematic()
# print("Arithematic =",result)

# def arithematic(a, b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# # positional argument
# result = arithematic(5,5)
# print("Arithematic =",result)

#keyword argument(Keyword name and parameter name must be same)
# def credential(username, password) :
#     if username == password:
#         print("Login Successfully")
#     else:
#         print("Invalid Credentials")
# credential(username="admin", password="admin")

# #default argument
# def cityName(city="Pune"):
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai")
# cityName()

#variable length argument/ Variable number of argument
# def cityName(*name):
#     print(name)

# cityName("Nagpur", "Delhi", "Mumbai", "Pune")

#modularity Approach in Function
# import sys
# def add():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a+b)
# def sub():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a-b)
# def mul():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a*b)
# def div():
#     a = int(input("Enter the value of A: "))
#     b = int(input("Enter the value of B: "))
#     print(a/b)
# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         add()#calling Function
#     elif choice == 2:
#         sub()#calling Function
#     elif choice == 3:
#         mul()#calling Function
#     elif choice == 4:
#         div()#calling Function
#     elif choice == 5:
#         sys.exit()

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)

sampleArray = [5,7,9,2,3,4]
findBiggestNumber(sampleArray)