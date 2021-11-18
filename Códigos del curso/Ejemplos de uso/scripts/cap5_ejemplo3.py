__author__ = 'febel'
t=[10,20,14,25,17,8,10,12,15,5,41,19,2,6,21]
i=0
encontrado=False
busq=15
while i < len(t) and not encontrado:
    if t[i]==busq:
        encontrado=True
    i=i+1
if encontrado:
    print("Encontrado en la posición",i-1)
else:
    print("")
