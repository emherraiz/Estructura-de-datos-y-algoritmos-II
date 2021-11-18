__author__ = 'febel'
tab=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
esta_ordenado=True
i=0
while i<19 and esta_ordenado:
    esta_ordenado=tab[i]<=tab[i+1]
    i=i+1
if esta_ordenado:
    print("Ordenado")
else:
    print("No ordenado")