# salary = int(input("Enter your salary :"))
# rating = int(input("Enter your performance appraisal rating :"))
# increment = 0
# if rating >= 1 and rating <= 3:
#     increment = salary*10/100
# elif rating>3.1 and rating<=4:
#     increment = salary*30/100
# elif rating>4.1 and rating<=5:
#     increment = salary*40/100   
# else:
#     print('Invalid rating')
# print('Incremented Salary: ', increment+salary)

# Salary calculation
# basicSalary = 20000
# HRA = 20/100 * 20000
# TA = 30/100 * 20000
# DA = 45/100 * 20000
# grossSalary = basicSalary - HRA - TA - DA
# print(grossSalary)

# def binarySearch(array, target):
#     low = 0
#     high = len(array)- 1
#     while low <= high:
#         mid = (low + high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low = mid+1
#         else:
#             high = mid - 1
#     return -1

# array = [2,4,9,5,9,11,13,14,15,16,17,19,24,27,29,33,36,38,42,47,48,49,51,58,62,69,72,79,82,84,86,88,89,91,94,99]
# target = 72
# result = binarySearch(array, target)
# if result == -1:
#     print("Element no found")
# else:
#     print("Element found at", result)

# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = temp
#             print(array)
#         print()

# array = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(array)

# array = input("Enter the array: ")
# count = -1
# for i in range(len(array)-1):
#     for j in range(len(array)-i-1, i+1):
#         if array[i] == array[j]:
#             count += 1
#     print(count)

# class Name:
#     age = 30# data member
#     def display(self): #method
#         print("Hello World")

# obj = Name() #reference variable
# print(obj.age)
# obj.display()/

# class Studen:
#     def __init__(self):
#         self.name = "Shreya"
#         self.age = 30

#     def display(self):
#         print("Name=", self.name)
#         print("Age=", self.age)
# stuObj = Studen()
# print(stuObj)

# class Message:
#     def __init__(self):
#         print("I am a constructor")

#     def show(self):
#         print("class program")

# obj = Message()
# obj.show()
# obj2 = Message()

#parameterised constructor
# class StudentInfo:
#     def __init__(self, name, age, roo_no):
#         self.Name = name
#         self.Age = age
#         self.RollNo = roo_no
#     def displayStudentInfo(self):
#         print("Name=", self.Name)
#         print("Age=", self.Age)
        
# studentObj = StudentInfo("Prakash", 34,101)
# studentObj.displayStudentInfo()

# import sys
# class Stack:
#     def __init__(self):
#         self.myStack = []

#     def push(self, value):
#         self.myStack.append(value)
#         print("Element push")

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False

#     def Pop(self):
#         if self.isEmpty():
#             print("Cannot pop element")
#         else:
#             print(self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print("the top most element of stack is: ",self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = None

#     def display(self):
#         print(self.myStack)
# obj = Stack()
# print("Stack has created :")
# while True:
#     print("1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop operation")
#     print("4. Peek operation")
#     print("5. Delete Stack")
#     print("7. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("Enter value to push in stack :"))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.Pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     else:
#         sys.exit()

import sys
class Stack:
    def __init__(self, L):
        self.myStack = []
        self.stackL = L
    def isFull(self) :
        if len(self.myStack) == self.stackL:
            return True
        else:
            return False


    def push(self, value):
        if self.isFull():
            print("Stack is full")
        else:
            self.myStack.append(value)
            print("Element push")

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False

    def Pop(self):
        if self.isEmpty():
            print("Cannot pop element")
        else:
            print(self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("the top most element of stack is: ",self.myStack[-1])

    def deleteStack(self):
        self.myStack = None

    def display(self):
        print(self.myStack)

L = int(input(print("Provide limit of stack :")))
obj = Stack(L)
print("Stack has created :")

while True:
    print("1. Push Operation")
    print("2. Display Stack")
    print("3. Pop operation")
    print("4. Peek operation")
    print("5. Delete Stack")
    print("7. Exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        value = int(input("Enter value to push in stack :"))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.Pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    else:
        sys.exit()