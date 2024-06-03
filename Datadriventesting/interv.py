# l1=[1,2,3,4,5,7,10,12]
# s1="abcde"
# n = len(l1)
# for i in range(n):
#     if i < len(s1):
#         a = str(l1[i]) + "*" + s1[i]
#         print(a)
#     else:
#         print(l1[i])
# def maximum(a, b):
#     if a >= b:
#         print(a," is maximum")
#     else:
#         print(b,"is maximum")
# # a = int(input("Enter a number: "))
# # # input1: 2
# # b = int(input("Enter a number: "))
# # input2: 4
# maximum(20,30)
# Write a program to check if the given strings are anagram or not.
def Anogram_check(str1, str2):
    # Strings are sorted and check whether both are matching or not
    if (sorted(str1) == sorted(str2)):
        print("Both strings are an Anagram.")
    else:
        print("Both strings are not an Anagram.")

Anogram_check('has','ash')
