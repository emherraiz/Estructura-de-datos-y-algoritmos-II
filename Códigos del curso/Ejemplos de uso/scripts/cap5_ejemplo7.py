t=[14,13,12,11,10,9,8,7,6,5,4,3,2,1]
permut=True
Cnt=len(t)-1
while permut:
    for i in range(0,len(t)):
        print(t[i],end=" ")
    print(" ")
    print("->")
    permut=False
    for i in range(0,Cnt):
        if t[i] > t[i+1]:
            temp=t[i]
            t[i]=t[i+1]
            t[i+1]=temp
            permut=True
    Cnt=Cnt-1
    for i in range(0,len(t)):
        print(t[i]," ",end=" ")
    print(" ")
