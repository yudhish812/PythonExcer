# Map function implementation
# lis=["2","35","65"]
# lis=list(map(int,lis))
# # for item in range(len(lis)):
# #     lis[item]=int(lis[item])
# for i in range(len(lis)):
#     lis[i]=lis[i]+5
#     print(lis[i])

# num=[2,3,6,89,21]

# def sq(a):
#     return a*a
# num=list(map(sq,num))
# print(num)

# num=list(map(lambda a:a*a,num))
# print(num)

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# def po4(a):
#     return a*a*a*a
#
# func=[sq,cube,po4]
#
# for i in range(5):
#     val=list(map(lambda a:a(i),func))
#     print(val)

# filter function implementation

# lis=[1,2,3,4,5,6,8,9]
# def is_greater_5(a):
#     return a>5
# greater_than_5=list(filter(is_greater_5,lis))
# print(greater_than_5)

# Implementation of Recduce
from functools import reduce
num=[1,2,3,4,5]
num=reduce(lambda x,y:x*y,num)
print(num)