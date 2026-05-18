# mydict = {
#     101 : "prashant",
#     102: "ashish",
#     "103":"mohini",
#     "104" : "trivani",
#     101: "ashish",
#     104 : "ashish"
# }
# print(mydict)
#with the help of key we have to print the value
# a = mydict[102]
# print(a)

#we will replace the old value with the new value
# mydict[102] = "peter"
# print(mydict)

#only print kae x=0,1
# for x in mydict:
#     print(x)
#only print values
# for x in mydict.values():
#     print(x)
# Printing key and values both
# for x,y in mydict.items():
#     print(x,y)

#adding a new key : value pair
# mydict["mobile_no"] = 4646463738
# print(mydict)

#pop method
# mydict.pop(101)
# print(mydict)

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a = {'a':1, 'b':2, 'c':3}
# print(a['a','b'])

# arr ={}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 1
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict = {'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print (dict[_])

# rec = {"Name" : "Python","Age" : "20"}
# r= rec.copy()
# print(id(r))
# print(id(rec))
# print(id(r) == id(rec))

# rec = {"Name" : "Python","Age" : "20"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"Name" : "Python","Age" : "20"}
# id2 = id(rec)
# print(id2)
# print(id1==id2)

# dic = {"A" : 50, "B": 30, "C" : 70}
# for _ in sorted(dic):
#     print(dic[_])

##important
# ip = [1,2,2,3,4,3,5]
# for i in ip:
#     count = count ip[i]
# if 

# num = 123456
# print(num)
# a = num % 10
# num = num//10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num%10
# num = num // 10
# f = num % 10
# rev = a*100000 + b*10000 + c*1000 + d*100+ e*10 + f
# print(rev)

#CHANGE OF CURRENCY
Amount = int(input("Please Enter Amount for Withdraw :"))
print(" 100 notes = ", Amount // 100)
print(" 50 Notes= ",(Amount % 100) // 50)
print(" 20 Notes= ",((Amount % 100) % 50) // 20)
print(" 10 Notes= ",(((Amount % 100) % 50) % 20) // 10)
print(" 5 Notes= ",((((Amount % 100) % 50) % 20) % 10) // 5)
print(" 2 Notes= ",(((((Amount % 100) % 50) % 20) % 10) % 5) // 2)
print(" 1 Notes= ",((((((Amount % 100) % 50) % 20) % 10) % 5) %2) // 1)