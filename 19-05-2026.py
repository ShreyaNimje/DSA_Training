#Find first non-repeating character from the string
# inpu = "leetcode"
# for i in range(len(inpu)):
#     for j in range(1, len(inpu)):
#         if i == j:
#             pass
#         else:
#             print(inpu[i])
#     j = i + 1

#------------------------------------------------------------------------------
#RECURRSION EXAMPLES
# Factorial Solution
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(4))
#------------------------------------------------------------------------------
#cpitalizeFirst Solution using recursion
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car', 'taco', 'banana']))

#------------------------------------------------------------------------------
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)
# print(power(2, 0))
# print(power(2, 2))
# print(power(2, 4))
#------------------------------------------------------------------------------

#product of Array
# def productofarray (arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productofarray(arr[1:])

# print(productofarray([1,2,3]))
# print(productofarray([1,2,3,10]))

#------------------------------------------------------------------------------
#reverse a string using recurrsion
# def reverse(strng):
#     if len(strng) <= 1:
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
# print(reverse('python'))
# print(reverse('appmillers'))

#------------------------------------------------------------------------------
#Recursive Range
# def recursiverange(num):
#     if num <= 0:
#         return 0
#     return num + recursiverange(num - 1)
# print(recursiverange(6))
#------------------------------------------------------------------------------
#Is Palindrome
# def ispalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return ispalindrome(strng[1:-1])
# print(ispalindrome('awesome'))
# print(ispalindrome('pop'))

#------------------------------------------------------------------------------
# somerecursive Solution
# def somerecursive(arr, cd):
#     if len(arr) == 0:
#         return False
#     if not(cd(arr[0])):
#         return somerecursive(arr[1:], cd)
#     return True
# def isOdd(num):
#     if num%2 == 0:
#         return False
#     else:
#         return True
    
# print(somerecursive([1,2,3,4], isOdd))
# print(somerecursive([4,6,8,9], isOdd))
# print(somerecursive([4,6,8], isOdd))

#------------------------------------------------------------------------------
# def max_product_sum(arr):
#     arr.sort()
#     num1, num2 = arr[-1], arr[-2]
#     return num1 + num2

# arr = [7, 9, 3, 8, 6, 7, 8, 10]
# print(max_product_sum(arr))  # Output: 19

#------------------------------------------------------------------------------
#Binary Tree
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child = []

#     def __str__(self, level = 0):
#         ret = " "*level + str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret

#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree node added")

# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee = Tree("Coffee")
# NonAlcoholi = Tree("Non Alcoholic")
# Alcoholic = Tree("Alcoholic")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcoholi)
# Cold.addChild(Alcoholic)

# print(rootNode)

#--------------------------------------------------------------------------------
# class Tree:
#     def __init__(self,data):
#         self.data = data
#         self.child = []

#     # del __str__ (self, level = 0):
#     #     ret = " "*level + str(self.data) + "\n"
#     #     for ch in self.child:
#     #         ret += ch.__str__(level+1)
#     #     return ret

#     def __str__(self, level=0):
#         ret = " " * level + str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level + 1)
#         return ret


#     def addChild(self, object):
#         self.child.append(object)
#         print("Tree node added")

# rootNode = Tree("N1")
# N2 = Tree("N2")
# N3 = Tree("N3")
# N4 = Tree("N4")
# N5 = Tree("N5")
# N6 = Tree("N6")
# N7 = Tree("N7")
# N8 = Tree("N8")

# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N6)
# N4.addChild(N7)
# N4.addChild(N8)

# print(rootNode)

#------------------------------------------------------------------------------
# Factorial Solution
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(4))

#------------------------------------------------------------------------------
# intp = [0, 0, 1, 2, 0, 3, 0, 0, 4]
# for i in intp:
#     if intp[i] == 0 and intp[i] == intp[0]:
#         intp.remove(0)
#     pass
# print(intp)

# intp = [0, 0, 1, 2, 0, 3, 0, 0, 4]

# while intp and intp[0] == 0:
#     intp.pop(0)

# print(intp)

#------------------------------------------------------------------------------
a = [1, 2, 3, 4, 5, 6]
B = [3, 4,-1, 1]
B = sorted(B)
for i in range(len(B)-1):
    for j in range(len(a)-1):
        if B[i] != a[j]:
            A = a[j]
        pass
    j = j+1
print(B)
print(A)
