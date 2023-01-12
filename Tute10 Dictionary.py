d1={}
# print(type(d1))
d2={"Yudhi":"Burger","Rohan":"Fish","skillF":"Roti","Shubham":{"B":"Chana","L":"roti","dinner":"Chicken"}}
# print(d2["Shubham"]["B"])
d2["Ankit"]="Junk Food"
d2[420]="Kabab"
del d2[420]
d3=d2.copy()
del d3["Yudhi"]
print(d2)
print(d3)