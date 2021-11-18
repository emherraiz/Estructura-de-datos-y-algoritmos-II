__author__ = 'febel'
t=[48,17,25,9,34,12,28,1,4,98,0,33,48,10,11,9,25]
n=0
Cnt=len(t)
while n<Cnt:
    n=3*n+1
while n != 0:
    n=n//3
    for i in range(n,Cnt):
        mem=t[i]
        j=i
        while j > (n-1) and t[j-n] > mem:
            t[j]=t[j-n]
            j=j-n
        t[j]=mem
    for j in range(0,Cnt):
        print(t[j],end=" ")
    print(" ")
