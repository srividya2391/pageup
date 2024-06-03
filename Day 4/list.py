mylist1=['a','b','c','d','e','f']
#print(mylist1)
for i in mylist1:
    if i=='c':
        continue
    print(i)
print("*************************************************")
print(len(mylist1))
print("*************************************************")
print(mylist1[1:3])
mylist1.append('z')
print(mylist1)
print("*************************************************")
mylist1.remove('a')
print(mylist1)
print("*************************************************")
mylist1.insert(0,'a')
print(mylist1)
print("*************************************************")
mylist1.clear()

