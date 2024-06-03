#print(a+b)
# a=10
# b=10 if we add comments for multiple line, the shortcut key is select all(ctrl+/)
def example(a, b, str): ## defining fun
    if str=="multiply":
        print(a*b)
    elif str=='add':
        print(a+b)
    elif str=='substract':
        print(a-b)
    elif str=='division':
        print(a/b)
    else:
        print('invalid operator')
    # for i in range(len(x)):  #for i in [0,1,2]
    #     print("############################")
    #     print(x[i])
    #     print("############################")
    #     y = x[i]+ x[i]
    #     print("=================================")
    #     print(y)
    #     print("=================================")
    #     z = str(x[i])+ str(x[i])
    #     print("**********************************")
    #     print(z)
    #     print("**********************************")
a = 3
b = 5
str = "multiply"
example(a, b, str)  ## calling func

