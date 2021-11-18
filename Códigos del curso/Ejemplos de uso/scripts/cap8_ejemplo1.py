__author__ = 'febel'

def tabla(tab):
    tab[1]=12345

t=[2,7,9,10,11,14,17,18,20,22]
copia=t
print(t[2])
copia[2]=5
print(t[2])
tabla(t)
print(t[1])