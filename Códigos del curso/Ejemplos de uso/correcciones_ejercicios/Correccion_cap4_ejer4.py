__author__ = 'febel'
inversion=150
presupuesto=31
semana=0

while inversion >= 0:
    semana=semana+1
    inversion-=presupuesto
    presupuesto=presupuesto*0.8
print(semana)