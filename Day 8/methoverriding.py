# class A:
#     def myfun(self):
#         print('welcome')
# class B(A):
#     def myfun(self):
#         print('python')
#         super().myfun() # method overriding
# obj1=B()
# obj1.myfun()
 ##### example 2 polymorphysm - method overloading
class A:
    def myfun(self,a=0,b=0):
        print(a+b)
obj1=A()
obj1.myfun()     ### overloading
obj1.myfun(20)
obj1.myfun(20,30)

