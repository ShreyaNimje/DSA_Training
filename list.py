# mylist = ["shreya", "Arya", "Komal","Ankush", "Arya", 77, "sandip", 60.52, "Shreya"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# mylist[2]="Akshay"
# print(mylist)

# if "Akshay" in mylist:
#     print("Akshay s available")
# else:
#     print("Akshay is not available")

# mylist.append("harsh")
# mylist.append('Ansh')
# print(mylist)

# mylist.insert(3, "Sanket")
# print(mylist)

# mylist.remove("sandip")
# print(mylist)

# newlist = mylist.copy()
# print(newlist)

# mylist = [['Shreya', 'Nimje'],['85.5'],[440022,"yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# # print(mylist[1][1])
# print(mylist[2][0])
# print(mylist[2][1])
            
# list2 = [50,25.50,'prashant']
# list2.clear()
# print (list2)

# name="Shreya"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[44,22,33,55,66,11]
# # mylist.sort()
# mylist.sort(reverse=True)
# print (mylist)
'''we should know that list should contain homogeneous data 
for sort function'''

# mylist=[44,22,33,55,66,11]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[44,22,33,55,66,11]
# for i in mylist:
#     print(i)

# list = [0,1,4,0,2,5]
# list.remove(0)
# list.append(0)
# list.remove(0)
# list.append(0)
# print(list)

# list1 = [0,1,4,0,2,5]
# for i in list1:
#     if i == 0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)/

# li = [7,3,9,2,8]
# li.sort()
# print(li[-2])

#MCQ-1
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10, 20, 30, 40, 50, 60
# print(a)
# # it will cerate a list as such [10,2,30,4,30,6,40,8,50] 60 is left
#MCQ-2
# a=[1,2,3,4,5]
# print(a[3:0:-1])
#MCQ-3
# arr =[[1,2,3,4],
#       [4,5,6,7],
#       [8,9,10,11],
#       [12,13,14,14]]
# for i in range(0,4):
#     print(arr[i].pop())

#MCQ-5
# fruit_list1 = ['Apple', 'berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)

#To find common elements in three arrays
# a= [1,2,3]
# b = [2,3,4]
# c = [3,4,5]
# for i in a:
#     if i in b and i in c:
#         print(i)

mylist =[]
N = int(input("Enter the value of N :"))
for i in range(N):
    val = int(input("Enter the value : "))
    mylist.append(val)
print(mylist)
sum = 0
for i in range(N-1):
    if i + 1 in range(N):
        sum += abs(mylist[i]-mylist[i+1])
print (sum)


# a = [10, 11, 7, 12, 14]
# sum = 0
# for i in a:
#     if i > 0:
#         sum += a[i]-a[i-1]
# print (sum)
