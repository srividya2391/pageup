def fun(a,b):
    if a>b:
        print(a,"greater than",b)
        print(type(a))
    else:
        print(b,"greater than",a)
        print(type(b))
    print(a+b)
a=input("enter a number for a =")
print(type(a))
b=input("enter number for b =")
fun(int (a),int (b))
