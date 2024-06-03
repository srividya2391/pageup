mytuple1=('sun','mon','tue','wed','thr','fri','sat')   ### this is the tuple
#print(len(mytuple1)) # to check the len of tuple
mylist1=list(mytuple1)
mylist1[1]='one'
mytuple1=tuple(mylist1)
print(mytuple1)
# if 'mon' in mytuple1:   ### to check the value exist in tuple or not
#     print("Monday")
# else:
#     print('no monday is not present')
# ########### example 2 : cope 2 tuples.
# #mytuple2=('one','two','three','four','five','six')
# mytuple2=mytuple1
# print(mytuple2)

# print('************************************')
# print(len(mylist1))
# #print('************************************')
# #print(type(mytuple1[1]))
# print('************************************')
# print(mylist1[3:5])
# print('************************************')
# #mytuple2=('one','two','three','four')
# #for i in mytuple2:
#    # print