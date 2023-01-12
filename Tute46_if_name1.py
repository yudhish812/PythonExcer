import sklearn

def printyu(str):
    return f"This is returning {str}"
def add(a,b):
    return a+b+5
print(f"name of this code is {__name__}")
if __name__=='__main__':
    print(printyu("Yudhi"))
    o=add(2,3)
    print(o)