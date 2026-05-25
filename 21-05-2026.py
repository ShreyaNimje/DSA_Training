#Stack implementation using a linked list
# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

    
#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Stack:
#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x.value) for x in self.LinkedList]
#         return'\n'.join(values)
#         # values = []
#         # temp = self.LinkedList.head
#         # while temp:                 # traverse the linked list
#         #     values.append(str(temp.value))
#         #     temp = temp.next
#         # return '\n'.join(values) 

#     def isEmpty(self):
#         if self.LinkedList.head == None:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             return "There is no any element in the Stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             self.LinkedList.head = self.LinkedList.head.next
#             return nodeValue
        
#     def peek(self):
#         if self.isEmpty():
#             return "There is no element in stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             return nodeValue

#     def push(self, value):
#         node = Node(value)
#         node.next =  self.LinkedList.head
#         self.LinkedList.head = node

# customStack = Stack()
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# customStack.push(4)
# print(customStack)
# print("Display the top value: ")
# print(customStack.peek())
# print("Pop top element")
# print(customStack.pop())
# print("Now check the stack again")
# print(customStack)
# print("Pop top element")
# print(customStack.pop())
# print("Now check the stack again")
# print(customStack)

#----------------------------------------------------------------------------
#Queue using a linked list
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Queue:
#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x) for x in self.LinkedList]
#         return ' '.join(values)
    
#     def enqueue(self, value):
#         newnode = Node(value)
#         if self.LinkedList.head == None:
#             self.LinkedList.head = newnode
#             self.LinkedList.tail = newnode
#         else:
#             self.LinkedList.tail.next = newnode
#             self.LinkedList.tail = newnode

#     def isEmpty(self):
#         if self.LinkedList.head == None:
#             return True
#         else:
#             return False
        
#     def dequeue(self):
#         if self.isEmpty():
#             return "There is no Node in th Queue"
#         else:
#             tempNode = self.LinkedList.head
#             if self.LinkedList.head == self.LinkedList.tail:
#                 self.LinkedList.head = None
#                 self.LinkedList.tail = None
#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return tempNode
        
#     def peek(self):
#         if self.isEmpty():
#             return "There is no element in stack"
#         else:
#             return self.LinkedList.head

# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# custQueue.dequeue()
# print(custQueue)
# print("Peek Element")
# print(custQueue.peek())
# print(custQueue)
# custQueue.dequeue()
# print(custQueue)
# custQueue.dequeue()
# print(custQueue)

#----------------------------------------------------------------------------
#Tree Implementation[Adjacency list]
# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex]=[]
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex,":", self.adjacency_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False
    
#     # def remove_edge(self, vertex1, vertex2):
            # if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            #     try:
            #         self.adjacency_list[vertex1].remove(vertex2)
            #         return True
            #     except ValueError:
            #         return False
            # return False

    
#     def remove_vertex(self, vertex):
        # if vertex in self.adjacency_list:
        #     for other_vertex in list(self.adjacency_list[vertex]):
        #         self.adjacency_list[other_vertex].remove(vertex)
        #     del self.adjacency_list[vertex]
        #     return True
        # return False


# graph = Graph()
# graph.add_vertex("A")
# graph.add_vertex("B")
# graph.add_vertex("C")
# graph.add_vertex("D")
# graph.add_vertex("E")
# graph.print_graph()
# graph.add_edge("A","B")
# graph.add_edge("A","C")
# graph.add_edge("A","D")
# graph.add_edge("B","A")
# graph.add_edge("B","E")
# graph.add_edge("C","A")
# graph.add_edge("C","D")
# graph.add_edge("D", "A")
# graph.add_edge("D", "C")
# graph.add_edge("D", "E")
# graph.add_edge("E", "B")
# graph.add_edge("E", "D")
# graph.print_graph()
# graph.remove_vertex("E")
# graph.print_graph

#----------------------------------------------------------------------------
#OOPs Concept
#Static Method
# class Student:
#     @staticmethod
#     def get_personal_detail(firstname, lastname):
#         print("Your personal detail=", firstname,lastname)

#     @staticmethod
#     def contact_detail(mob_no, rollno):
#         print("Your contact detail=", mob_no, rollno)

# Student.get_personal_detail("Shreya", "Nimje")
# Student.contact_detail(7249566778, 10135)

#Garbage collector
#Destructor for resource reallocation
#Inheritance

#----------------------------------------------------------------------------
#Single level inheritance
# class College:
#     def College_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name: Shreya Nimje")
#         print("Branch: MCA")

# obj = Student()
# obj.College_name()
# obj.student_info()

#----------------------------------------------------------------------------
#Multilevel Inheritance
# class College:
#     def College_name(self):
#         print("Modern College")

# class Student(College):
#     def student_info(self):
#         print("Name: Shreya Nimje")
#         print("Branch: MCA")

# class Exam(Student):
#     def subject(self):
#         print("Subject1 : Design Engineering")
#         print("Subject2 : Math")
#         print("Subject3 : C")

# obj = Exam()
# obj.College_name()
# obj.student_info()
# obj.subject()

#----------------------------------------------------------------------------
#Multiple Inheritance
# class SubjMarks:
#     math = int(input("Enter Paper marks of maths :"))
#     DE = int(input("Enter paper marks for AI :"))
#     C = int(input("Enter paper marks for CyberSecurity :"))
#     eng = int(input("Enter paper marks for English :"))

# class PractMarks:
#     cpract = int(input("Enter practical marks for AI : "))

# class Result(SubjMarks, PractMarks):
#     print("If students pass in both practical and subject paper then pass")
#     def total(self):
#         if self.math>=40 and self.DE>= 40 and self.C>= 40 and self.eng>=40 and self.cpract>=20:
#             print("Pass")
#         else:
#             print("Fail")
# obj = Result
# obj.total()

#----------------------------------------------------------------------------
#Python only supports Operator Overloading
'''Suppose child class is not happy with parent class properties then it defines the same property by itself'''
# class Rbi:
#     def homeloan(self):
#         print("Home loan ROI = 8%")

#     def eduloan(self):
#         print("Education loan ROI = 9%")

# class Sbi(Rbi):
#     def eduloan(self):
#         print("Education loan ROI = 10%")

# obj = Sbi()
# obj.eduloan()

#to access parent class method as well
# class Rbi:
#     def homeloan(self):
#         print("Home loan ROI = 8%")

#     def eduloan(self):
#         print("Education loan ROI = 9%")

# class Sbi(Rbi):
#     def eduloan(self):
#         print("Education loan ROI = 10%")
#         super().eduloan()

# obj = Sbi()
# obj.eduloan()

#Contructor Overriding
class Rbi:
    def __init__(self):
        print("Parent Class constructor")

class Sbi(Rbi):
    def __init__(self):
        print("Child Class constructor")

obj = Sbi()