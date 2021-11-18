__author__ = 'febel'
t=[2,7,9,10,11,14,17,18,20,22]
busq=14
d=0
f=len(t)-1
while True:
    m=int((d+f)/2)
    print("d=",d,", f=",f,", m=",m," t[m]=",t[m])
    if busq > t[m]:
        d=m+1
    else:
        f=m-1
    if not(d<=f and busq !=t[m]):
        break
if busq==t[m]:
    print(busq," encontrado a la posición ",m)
else:
    print(busq," no se ha encontrado ")
