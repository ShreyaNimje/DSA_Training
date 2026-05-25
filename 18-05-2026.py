# a, b = [str(x) for x in input("Enter the String: ").split(" ")]
# a1 = ""
# a2 = ""
# for i in range(len(a)-1, -1, -1):
#     a1 += (a[i])

# for j in range(len(b)-1, -1, -1):
#     a2 += (b[j])
# print(a1 + " " +a2)

#_________________________________________________________________________#

#Insertion Sort
# import sys
# array = [5, 3, 8, 6, 2]
# for i in range(1, len(array)):
#     key = array[i]
#     j = i - 1
#     while j>= 0 and key < array[j]:
#         array[j + 1] = array[j]
#         j -= 1
#     array[j+1] = key
#     print (array)
# else:
#     sys.exit()

##Stackoverflow 2025 survey to check in demand technologies and profiles

#_________________________________________________________________________#

# import sys
# array = [5, 3, 8, 6, 2]
# for i in range(0, len(array)):
#     min = array[i]
#     j = i+1
#     while j <= len(array) and min > array[j]:
#         min = array[j]
#         j+= 1
#     min = array[i]
#     array[j+1] = min
#     print(array)
# else:
#     sys.exit()

# import sys
# array = [5, 3, 8, 6, 2]
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[j] < array[min_index]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
#     print(array)
# else:
#     sys.exit()

# import sys
# array = [5, 3, 8, 6, 2]
# for i in range(len(array)):
#     min_index = i
#     j = i+1
#     while j < len(array):
#         if array[j] < array[min_index]:
#             min_index = j
#         j = j+1
#     array[i], array[min_index] = array[min_index], array[i]
#     print(array)
# else:
#     sys.exit()
#_________________________________________________________________________#

# list = [int(input("Enter the elements :").split(" "))]
# N = len(list)
# dict = {}
# for i in 

#_________________________________________________________________________#

# si = {"C":3, "B":2, "A":1}
# print(si)

#_________________________________________________________________________#
#Instance Variable
# It depends on the 
# class New:
#     def __init__(self):
#         self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20   # Only Obj1 is changed
# print(Obj1.a)  # 20
# print(Obj2.a)  # 10
# print(Obj3.a)  # 10

# #Static Variable
# class New:
#     a = 10
#     def __init__(self):
#         self.name = "Shreya"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# #New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#Combination of static and instance variable
# class College:
#     collegename = "Modern College"
#     def __init__(self):
#         self.studentname = "Shreya"

# principal = College()
# teacher = College()
# accountant = College()
# print("principal=",principal.collegename,"....",principal.studentname)
# print("teacher=",teacher.collegename,"....",teacher.studentname)
# print("accountant=",accountant.collegename,"....",accountant.studentname)
# College.collegename = "RBU"
# principal.studentname = "Shreya Nimje"
# print("principal=",principal.collegename,"....",principal.studentname)
# print("teacher=",teacher.collegename,"....",teacher.studentname)
# print("accountant=",accountant.collegename,"....",accountant.studentname)

#_________________________________________________________________________#
#Linked List

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# linkedlist = LinkedList()

# linkedlist.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)
# #connecting the nodes
# linkedlist.head.next = second
# second.next = third
# third.next = fourth

# #Display of linked list
# while linkedlist.head != None:
#     print("|",linkedlist.head.data, linkedlist.head.next ,"|","->", end=" ")
#     linkedlist.head  = linkedlist.head.next

#_________________________________________________________________________#
import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail = self.node

    def addNodeBeginning(self, value):
        print("Add node in Beginning")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node

        

    #def addNodebetween(self, value, value1, value2):
    
        # print("Add Node in Between")
        # new_node = Node(value)
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node
        #     return
        # current = self.head
        # while current is not None and current.next is not None:
        #     if current.data == value1 and current.next.data == value2:
        #         # Insert new_node between current and current.next
        #         new_node.next = current.next
        #         current.next = new_node
        #         return
        #     current = current.next
        # print("Nodes with given values not found in sequence")
    def addNodebetween(self, value, index):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def display(self):
        while self.head != None:
            print("|",self.head.data,''' self.head.next ,'''"|","->", end=" ")
            self.head  = self.head.next

if __name__ == '__main__':
    object = LinkedList()
    while True:
        print('\n1. Add Node Linkedlist : ')
        print('2. Add Node in Begining : ')
        print('3. Add node in Between : ')
        print("4. Add Node in End : ")
        print('5. Display Linked List : ')
        print('6. Exit')
        ch = int(input('Enter Your Choice : '))
        if ch == 1:
            value = int(input('Enter value for node: '))
            object.addNode(value)
            print('Node added successfully in single LinkedList : ')
        elif ch == 2:
            value = int(input('Enter value for node: '))
            object.addNodeBeginning(value)
        elif ch ==3:
            value = int(input("Enter value for Node: "))
            index = int(input("Enter the position to insert the node : "))
            object.addNodebetween(value, index)
            
            # value1 = int(input("Enter the value of node before : "))
            # value2 = int(input("Enter the value of node after : "))
            # object.addNodebetween(value, value1, value2)
            
        elif ch == 5:
            object.display()
        else:
            sys.exit()