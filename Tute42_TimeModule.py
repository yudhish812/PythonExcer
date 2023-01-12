import time

initial=time.time()
print(initial)
k=0
while(k<45):
    print(f"count {k}")
    time.sleep(2)
    k+=1
timetaken=time.time_ns()-initial
print(timetaken)
initial1=time.time()
for i in range(45):
    print(f"count {i}")
timetaken1=time.time_ns()-initial1
print(timetaken1)
if timetaken==timetaken1:
    print("No difference")
else:
    print("Hmm.... interesting")

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)