__author__ = 'febel'
horas=17
minutos=55
segundos=48
numsec=int(input("¿Cuántos segundos adicionales?\n"))
segundos=segundos+numsec
if segundos > 59:
    minutos=minutos+(segundos/60)
    segundos=segundos%60
if minutos > 59:
    horas=horas+(minutos/60)
    minutos=minutos%60
    if horas > 23:
        dias=horas/24
        horas=horas%24
print(dias,"d ",horas,":",minutos,":",segundos)