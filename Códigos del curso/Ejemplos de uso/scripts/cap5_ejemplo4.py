__author__ = 'febel'
notas=[10,20,14,11,17,8,10,12,15,5,16,19,2,6,0]
i=0
min=notas[0]
max=notas[0]
med=0
for i in range(0,len(notas)):
    med=med+notas[i]
    if notas[i] > max:
        max=notas[i]
    if notas[i] < min:
        min=notas[i]
med=med/len(notas)
print(min," ",max," ",med)
