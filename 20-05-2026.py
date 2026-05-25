#Binary Search Tree
# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# def insernode(rootnode, nodevalue):
#     if rootnode.data == None:
#         rootnode.data = nodevalue
#     elif nodevalue <= rootnode.data:
#         if rootnode.leftchild is None:
#             rootnode.leftchild = BSTNode(nodevalue)
#         else:
#             insernode(rootnode.leftchild, nodevalue)
#     else:
#         if rootnode.rightchild is None:
#             rootnode.rightchild = BSTNode(nodevalue)
#         else:
#             insernode(rootnode.rightchild, nodevalue)

# def searchnode(rootnode, nodevalue):
#     if rootnode.data == nodevalue:
#         print("The value is found at", rootnode.data)
#     elif nodevalue <= rootnode.data:
#         if rootnode.leftchild == nodevalue:
#             print("The value is found at", rootnode.leftchild)
#         elif rootnode.leftchild == nodevalue:
#             searchnode(rootnode.leftchild, nodevalue)
#         else:
#             print("Value not found")
#     elif nodevalue >= rootnode.data:
#         if rootnode.rightchild == nodevalue:
#             print("The value is found")
#         elif rootnode.leftchild == nodevalue:
#             searchnode(rootnode.rightchild, nodevalue)
#         else:
#             print("Value not found")
#     # else:
#     #     print("Value not found")

# def preOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     print(rootnode.data, end=" ")
#     preOrderTraversal(rootnode.leftchild)
#     preOrderTraversal(rootnode.rightchild)

# def InOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     InOrderTraversal(rootnode.leftchild)
#     print(rootnode.data, end=" ")
#     InOrderTraversal(rootnode.rightchild)

# def PostOrderTraversal(rootnode):
#     if not rootnode:
#         return
#     PostOrderTraversal(rootnode.leftchild)
#     PostOrderTraversal(rootnode.rightchild)
#     print(rootnode.data, end=" ")

# newBST = BSTNode(None)
# insernode(newBST, 70) 
# insernode(newBST, 50)
# insernode(newBST, 90) 
# insernode(newBST, 30)
# insernode(newBST, 60) 
# insernode(newBST, 80)
# insernode(newBST, 100) 
# insernode(newBST, 20)
# insernode(newBST, 40)
# insernode(newBST, 10)
# preOrderTraversal(newBST)
# print()
# InOrderTraversal(newBST)
# print()
# PostOrderTraversal(newBST)
# print()
# searchnode(newBST, 5)

#---------------------------------------------------------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# try:
#     print(a/b)
# except:
#     print("Can't devide by zero")


# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't devide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# except:
#     print("ABC")

#-- Can we take multiple exceptions in single except block??
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

#-- Can we take else block in except block, and when will it execute??
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't devide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# else:
#     print("Everything is okay")

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't devide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# finally:
#     print("I always executed")

#---------------------------------------------------------------------
# import logging
# logging.basicConfig(filename="newfile.txt", level = logging.DEBUG)
# try:
#     a = int(input("enter first integer numbet: "))
#     b = int(input("enter second integer numbet: "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up. Check 'newfile.txt' for log details. ")

#---------------------------------------------------------------------
'''If file is open and we execute the code it throws a permission denied error'''
# import csv
# f = open("employee.csv",'a')
# a = csv.writer(f)
# #a.writerow(["EmpId","Emp Name","Emp Age"])
# empid = int(input("Enter your empid: "))
# empname = input("enter employee name: ")
# age = int(input("Enter employee age: "))
# a.writerow([empid,empname,age])
# print("FData has been added")

#---------------------------------------------------------------------
#Column name = stuId |studName | phy | chem | Maths | Total| Percentage | Result
# user input = stuId |studName | phy | chem | Maths
# calculate = total, percentage
#check condition all paper marks >= 40 pass else fail
import csv
f = open("Result.csv",'a')
a = csv.writer(f)
a.writerow(["stuId","studName","phy","chem","Maths","Total","Percentage","Result"])
Stuid = int(input("Enter your stuid: "))
empname = input("enter student name: ")
Phy = int(input("Enter Physics marks: "))
Phy2 = int(input("Enter Chemistry marks: "))
Phy3 = int(input("Enter Maths marks: "))
total = (Phy + Phy2 + Phy3)
percent = (total/300)
result = "Pass" if percent >= 40 else "Fail"
a.writerow([Stuid, empname, Phy, Phy2, Phy3, total, percent, result])
print("Student record added successfully!")