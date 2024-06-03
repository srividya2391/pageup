### create a dictionary#########
dick1={101:'y',102:'x',103:'z'} # key:'value'
dick2={1:'a',2:'b',3:'c'}
# print(dick1) #### printing the dictionary items
# print((dick1[101],dick1[102])) # accessing the itme from dictionary here
# print(len(dick1))
# x=print(dick1.get(101)) # using get fuction
#  ##### reading a item of dictionary using loop
# for i in dick1:
#     print(i)  # reading the keys
# for x,y in dick1.items(): # reading items along with keys
#     print(x,y)
# if 101 in dick1: # checking the value exist in dick
#     print('exist')
# else:
#     print('not exist')
 # add items to dick
dick1[404]='k'
print(dick1)
# remove item form dick
dick2.pop(3)
print(dick2)
#del dick2
#print(dick2)
dick1.clear()
print(dick1)
