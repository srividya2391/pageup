# a,b,c= 40,40,50
# class a:
#
#     def myfun(self,a,b,c):
#         print(a+b+c)
#         print(self.x*self.y)
#
# k=a()
# k.myfun(a=40,b=40,c=50)
class emp:
    def __init__(self,eid,name,sal):
        print(eid,name,sal)
    def display(self,name):
        return(name)
a=emp(101,"sawathi",300000)
print(a.display("swathi"))

