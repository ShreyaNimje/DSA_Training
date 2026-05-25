# import re
# count = 0
# pattern = re.compile("function")
# print(pattern)

# matcher = pattern.finditer("A function in python is defined by a def statement. In python the general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters.")
# for i in matcher:
#     count += 1
#     print(i.start(),"....", i.end(),"....", i.group())
# print("The number of occurences: ",count)

#--------------------------------------------------------------------
# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count += 1
#     print(i.start(),"....", i.end(),"....", i.group())
# print("The number of occurences: ",count)

#--------------------------------------------------------------------

# import re
# obj = input("enter any charecter")
# objmatch = re.finditer(obj, "a7b @k9z")
# print(objmatch)
# for match in objmatch:
#     print(match.start(),"...", match.end(),"...", match.group)

#--------------------------------------------------------------------
# import re
# a = input("Enter the string to perform match operation: ")
# mtch = re.match(a, "python is very important language")
# print(mtch)
# if mtch != None:
#     print("match found at begining level")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("there is no matching at the beginning level")

#--------------------------------------------------------------------
# import re
# a = input("Enter the string to perform match operation: ")
# mtch = re.fullmatch(a, "pythonisvery")
# print(mtch)
# if mtch != None:
#     print("match found ")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("full match not found")

#--------------------------------------------------------------------
# import re
# s = input("Enter Mail-id: ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!= None:
#     print("Valid E-Mail Id")
# else:
#     print("Invalid Email id")

#--------------------------------------------------------------------
# import re
# mo = input("Enter Mobile number: ")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj!= None:
#     print("Valid Mobile number")
# else:
#     print("Invalid Mobile number")

#--------------------------------------------------------------------
#Search Function
# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.search(a, "Python is very dynamic language")
# print(mtch)
# if mtch!= None:
#     print(mtch.start()," ", mtch.end()," ", mtch.group())
# else:
#     print("there is no match anywhere")

#--------------------------------------------------------------------
# import re
# mtch = re.findall('[A-Z]',"abdgh56& 78hn @()")
# print(mtch)

#--------------------------------------------------------------------
#sub() function
# import re
# obj = re.sub('[a-z]','*','2345 ABCD habc deff')
# print(obj)

#--------------------------------------------------------------------
#subn() function
# import re
# obj = re.subn('[a-z]','*','2345 ABCD habc deff')
# print(obj)
# print("The string is: ",obj[0])
# print("the number of replacement is =",obj[1])

#--------------------------------------------------------------------
#Task 1
# import re
# f1 = open("file.txt", "r")
# content = f1.read()
# mtch = re.findall("anti", content)
# print(mtch)
# f1.close()

#--------------------------------------------------------------------
# import os, sys
# fname = input("Enter file name: ")
# if os.path.isfile(fname):
#     print("File exists: ", fname)
#     f = open(fname, "r")
# else:
#     print("file does not exists: ",fname)
#     sys.exit(0)
# lcount = wcount = ccount = 0
# for line in f:
#     lcount = lcount+1
#     ccount = ccount+len(line)
#     words = line.split()
#     wcount= wcount+ len(words)
# print("The number of line: ", lcount)
# print("The number of words: ",wcount)
# print("The number of characters: ",ccount)

#--------------------------------------------------------------------
# Adjacency Matrix
class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.V = vertices
        #Create adjacency matrix with all 0s
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]
        
    #Add edge between two vertices
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
        
    #Display Matrix
    def display(self):
        for row in self.matrix:
            print(row)

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

#Create a graph with 4 vertices
g = Graph(4)
#Add Edge
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)

print("Adjacency Matrix")
g.display()

#--------------------------------------------------------------------
#Hashing
class HashTable:
    def __init__(self, size):
        self.size = size
        size.table = [[] for _ in range(size)]

    def hash_function(self,key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)

from collections import Counter
def missingNumbers(arr, brr):
    c1 = Counter(arr)
    c2 = Counter(brr)
    
    result = {}
    
    for num in c2:
        if c2[num] != c1[num]:
            result.append(num)
    return sorted(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
