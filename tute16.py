# list1=["Harry","Larry","Carry","Marie"]
#
# for item in list1:
#     print(item)

list1=[["Harry","1"],["Larry","1"],["Carry","35"],["Marie","250"]]
dict1=dict(list1)
print(dict1)
for item, lolly in dict1.items():
    print(item,"and Lollys are",lolly)