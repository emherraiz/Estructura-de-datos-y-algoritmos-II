__author__ = 'febel'
t=[48,17,25,9,34]
Cnt=len(t)
for i in range(1,Cnt):
    mem=t[i]
    pos=i-1
    while pos >=0 and t[pos]>mem:
        t[pos+1]=t[pos]
        pos=pos-1
    t[pos+1]=mem
    for j in range(0,Cnt):
        print(t[j],end=" ")
    print(" ")
