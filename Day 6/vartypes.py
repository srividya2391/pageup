# # global variable
# x=300 # global variables
# #local variables
# def myfun():
#     local_x=20
#     global x
#     x=200 # x is a globval variable
#     print(local_x)
# myfun()
# print(x)
############# example 2
# x=100
# def myfun():
#     global x
#     x=300
#     print(x)
# myfun()
# print(x)    # we already changed a value with the function so this x is defaulted to new chaged value
x=100
def myfun():
    global x
    x=300
    print(x)
# myfun()
print(x)