__author__ = 'febel'
t=[27,44,12,18,23,19,101,54,29,77,52,88,10,32]
Cnt=len(t)
for i in range(0,Cnt-1):
    min=i
    for j in range(i+1,Cnt):
        if t[j] < t[min]:
            min=j
    if min != 1:
        temp=t[min]
        t[min]=t[i]
        t[i]=temp
    for j in range(0,Cnt):
        print(t[j]," ",end=" ")
    print("\n")
