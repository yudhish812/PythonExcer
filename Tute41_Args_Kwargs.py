# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("Yu","Ma","Ba","Ri")
def func(a,*args,**kwargs):
    print(a)
    for item in args:
        print(*args)
    for key, value in kwargs.items():
        print(f"{key} is {value}")
lst=["Yu","Ma","Ba","Ri"]
kw={"Ri":"Didi","YU":"Bade","Ma":"2nd","Ba":"third"}
b=32
func(b,*lst,**kw)