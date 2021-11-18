__author__ = 'febel'
t=[48,17,25,9,34,59,8,1,27,65,44,2,100]
cont=len(t)
creciente=False
for i in range(1,cont):
    mem=t[i]
    pos=i-1
    while (pos>=0 and ((creciente and t[pos]>mem) or (not creciente and t[pos]<mem))):
        t[pos+1]=t[pos]
        pos=pos-1
    t[pos+1]=mem
for j in range(0,cont):
    print(t[j],end= " ")
print(" ")
