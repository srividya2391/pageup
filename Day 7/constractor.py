# example for constractor
# class emp:
#     def __init__(self): # constractor creation
#         print('name')
# k=emp()
####### example 2
class emp:
    x,y=10,15      # global variables
    def __init__(self,a,b): # local variables
        print(a+b)
        print(self.x+self.y)
obj1=emp(20,50)
########## example 3
# class emp:
#     def __init__(self,eid,ename,sal):
#         print(eid,ename,sal)
#     def display(self,eid,ename,sal):
#         print(eid,ename,sal)
# obj1=emp(101,'swathi',400000)
# obj1.display(101,'swathi',450000)
# obj2=emp(201,'srividya',30000)
# obj2.display(101,'srividya',450000)

# # example 4
# class emp:
#     name='swathi'
#     def __str__(self):
#         return(self.name)
# k=emp()
# print(k)


