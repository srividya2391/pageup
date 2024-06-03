# # example 1
# class employee:
#     def myfun(self,name,age,sal):
#        print(name,age,sal)
# x=employee()   ### instant method, we can call only throught object here x is the object
# x.myfun('swathi',33,40000)
#example 2 Sattic method
# class emp:
#     @staticmethod
#     def myfun(self,name,dep,age):
#         print(self,name,dep,age)
# emp().myfun('myself','swathi','testing',33) ### static method- we can directly call using class
# example 4
# class emp:
#     a,b=10,15   # class variables
#     def add(self):
#         print(self.a + self.b)
# a=emp()
# a.add()
####### example 4
# i,j=40,50   # global variables
# class emp:
#     a,b=10,20    # class variables
#     def add(self,x,y):  # local variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# k=emp()
# k.add(100,200)
# one class with multiple object
class emp:
    def myfun(self,name):
        print(name)
obj1=emp()
obj1.myfun("swathi")
obj2=emp()
obj2.myfun('srividya')



