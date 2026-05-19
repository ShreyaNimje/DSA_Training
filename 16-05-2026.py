#Question 1
# import math
# A = int(input("Enter the number of plots available: "))
# Arr = []

# for i in range (A):
#     element = int(input("Enter the areas: "))
#     Arr.append(element)

# #for i in range (A):
#     #if num = math.isqrt(num)8
# for i in range(A):
#     print(A[i])

# def func(value, values):
#     var = 1
#     values[0] = 44
# t = 3 
# v = [1, 2, 3]
# func(t, v)
# print(t, v[0])

# def f(i, values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

#queue datastructure
# 1. EnQueue --> Add element
# 2. DeQueue --> Delete element
# 3. Display Queue
# 4. IsEmpty
# 5. IsFull()
# 6. Delete
# 7. Queue

# import sys
# class Queue:
#     def __init__(self, size):
#         self.myQueue = []
#         self.queueSize = size

#     def isFull(self):
#         if len(self.myQueue) == size:
#             return True
#         else: 
#             return False
        
#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False
    
#     def display(self):
#         print(self.myQueue)

#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             self.myQueue.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue[0])

#     def delete(self):
#         self.myQueue = None


# size = int(input("Enter the size of queue :"))
# obj = Queue(size)
# print("Stack has created :")
# while True:
#     print("1. Enqueue Operation :")
#     print("2. Display Queue :")
#     print("3. Delete Operation :")
#     print("4. Peek Operation :")
#     print("5. Delete Queue :")
#     print("6. Exit :")
#     choice = int(input("Enter Your choice :"))

#     if choice == 1:
#         value = int(input("Enter element to add in queue: "))
#         obj.enQueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.dequeue()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.delete()
#     else:
#         sys.exit()

#Stack using List
# -- Easy to implement
# -- Speed problem when it grows
#Stack using linked list
# -- Hard to implement
# -- Implementation is not easy

# fruit ={} #{'apple':1, 'Banana':1, 'Apple':1}
# def addone (index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('apple')
# addone('Banana')
# addone('Apple')
# print(len(fruit))

'''Write a program to accept student name and marks from the keyboard and 
create a dictionary. Also display student marks by student name'''
# n = int(input("Enter number of students: "))
# student = {}
# for i in range(n):
#     name = input("Enter Student name: ")
#     marks = input("Enter Student Marks: ")
#     student[name] = marks #add key:value
# while True:
#     name = input("Enter Student Name to get marks: ")
#     marks = student.get(name, -1)
#     if marks == -1:
#         print("Student not Found")
#     else:
#         print("The Marks of", name,"are", marks)
#     option = input("Do you want to find another student marks[Yes|No]")
#     if option == "No":
#         break
# print("Thanks for using our application")

'''Write a program to access each character of string in forward and backward
direction by using the while loop

i/p = "Learning python is very easy".'''

# str = "Learning python is very easy"
# n = len(str)
# i = 0 
# print("Forward Direction")
# while i <n:
#     print(str[i],end=' ')
#     i += 1
# print()
# print("Backward Direction")
# i = -1
# while i >= -n:
#     print(str[i], end=' ')
#     i = i-1

#------------------------------------------------------------------------#

#i/p :- abcdfigerj abcdfiger
#o/p :- j

# input = "abcdfjgerj abcdfiger"
# for i in range(len(input)):
#     for j in range(len(input)-1,-1,-1):
#         if input[i] == input[j]:
#             pass
#         else:
#             miss = input[j]
# print(miss)

#______________________________________________________________________________#
# v = ['a','e', 'i','o','u']
# w = input("Enter the string to search vowels into :")
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found',found)
# print('Unique vowels',len(found),'from the given word =',w)

#*******************************************************************************#
# a, b, c = map(int,input("--").split())
# list = []
# for i in range(a):
#     x = int(input())
#     list.append(x)

# for j in list:
#     if j >= b and j<= c:
#         print(j, end=" ")

'''--6 30 50
29
38
12
48
39
55
38 48 39 '''
#*******************************************************************************#
# import datetime
# #datetime formatting
# date=datetime.datetime.now()
# print("It's now: {:%d/%m/%Y %H:%M:%S}".format(date))

#_______________________________________________________________________________#
# x =['A','B','C']
# y =['A','B','C']
# z = [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

#_______________________________________________________________________________#
#List Compression
# s = [i*i for i in range(1,11)]
# print(s)
# s = [1,4,9,16,25,36,49,64,81,100]
# val = [2**i for i in range(1,6)]
# print(val)

#_______________________________________________________________________________#
#Dictionary Comprehension:
# squares = {x:x*x for x in range(1,6)}
# print(squares)

# doubles = {x:2*x for x in range(1,6)}
# print(doubles)

#How to read multiple values from the keyboard in a single line:
# a,b = [int(x) for x in input("Enter 2 numbers :").split()]
# print("Product is :", a*b)

# a,b,c =[float(x) for x in input("Enter three float numbers :").split(' ')]
# print("The sum is :", a+b+c)
#_______________________________________________________________________________#
# mycart = [10,20,800,60,70]
# for item in mycart:
#     if item > 400:
#         print("Not in my Budget!!")
#         continue
#     print(item)
# else:
#         print("you have purchased everything")

#_______________________________________________________________________________#
# import sys
# username = "admin"
# password = "admin"
# while True:
#     user = input("Enter username :")
#     passw = input("Enter password :")
#     if username == user and password == passw:
#         print("User logged in!!")
#         break
#     else:
#         continue
#_______________________________________________________________________________#
#Tower of Hannoi
import time
class Tower:
    def __init__(self):
        print("Welcome to tower of hanoi game")
        print()
        print("Given Problem     A= [3, 2, 1]         B = []            C = []")
        print()
        print("Expected Output   A= []                B = []            C = [3,2,1]")
        self.A = []
        self.B = []
        self.C = []

    def tower(self, item):
        self.A.append(item)
        time.sleep(3)
        print("A=", self.A)
        print("Items in tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass One completed====================\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Two completed====================\n")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Three completed====================\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Four completed====================\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Five completed====================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Six completed====================\n")
    
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A    ,"    ",   "B=", self.B   ,"    ","C=",self.C)
        print("Pass Seven completed====================\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4() 
obj.pass5()
obj.pass6()
obj.pass7()