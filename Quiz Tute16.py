list1=["Ram", "Shyam", "16", "23","3", "Harry","40.7"]
for item in list1:
    if str(item).isnumeric() and str(item).is_float() and int(item)>6:
        print(item)
