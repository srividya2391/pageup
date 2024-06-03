myset= {'sun','mon','tue','wed','thr','fri'} ### creating a set
print(myset)
print(len(myset))
myset.add('sat')
print(myset)
print(myset[0,1])
###### accessing all values from the set
# for i in myset:
#     print(i)
######## to check item present or not
if 'sun' in myset:
    print('yes')
else:
    print('no')
