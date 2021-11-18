__author__ = 'febel'
t=[[1,2,3],[4,5,6,7],[8,9,10,11]]
total=0
for i in range(0,len(t)):
    total=total+len(t[i])
    print(len(t[i]))
print(total)
