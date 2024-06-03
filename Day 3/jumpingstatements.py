# ####### print 5 to 20 number with 5 incremental value and brek the value  for 10
# for i in range(0,5):
#     if i==2:           ##### i=5 >= 15
#         break
#     print(i)
# print('done!!!!!!')
########### continue
for i in range (0,10,2):
    if i==2 or i==4:
        continue
    print(i)
print("done!!!!!!!!!!!!!!!!!!!")
