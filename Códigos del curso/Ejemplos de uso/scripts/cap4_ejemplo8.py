__author__ = 'febel'
cantidad=1700
num500=0
while cantidad >= 500:
    num500=num500+1
    cantidad=cantidad - 500
print("Número de billetes de 500 :", num500)
print("Resto:",cantidad)