# single inheritance
# class K:
#     x,y=10,20
#     def myfun1(self):
#         print(self.x + self.y)
# class L(K):   ##### this is the child class of 'A'
#     a,b=50,40
#     def myfun2(self):
#         print(self.a * self.b)
# obj1=L()
# obj1.myfun1()
# obj1.myfun2()
###### example 2: multi level inheritance
# class A:
#     a,b=30,50
#     def myfun1(self):
#         print(self.a+self.b)
# class B(A):
#     i,j=30,60
#     def myfun2(self):
#         print(self.i*self.j)
# class C(B):
#     x,y= 40,30
#     def myfun3(self):
#         print(self.x-self.y)
# obj1=C()
# obj1.myfun1()
# obj1.myfun2()
# obj1.myfun3()
# Heirarchy inheritance
# class A:
#     x,y=20,70
#     def myfun(self):
#         print(self.x+self.y)
# class B(A):
#     a,b= 25,30
#     def myfun2(self):
#         print(self.a+self.b)
# class C(A):
#     i,j= 50,100
#     def myfun3(self):
#         print(self.i+self.j)
# obj1=B()
# obj1.myfun()
# obj1.myfun2()
# obj2=C()
# obj2.myfun()
# obj2.myfun3()

######## multiple inheritance
class A():
    a,b=30,50
    def myfun(self):
        print(self.a+self.b)
class B():
    x,y=40,50
    def myfun1(self):
        print(self.x+self.y)
class C(A,B):
    c,d=50,100
    def myfun2(self):
        print(self.c+self.d)
obj1=C()
obj1.myfun()
obj1.myfun1()
obj1.myfun2()





