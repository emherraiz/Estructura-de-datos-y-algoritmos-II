__author__ = 'febel'
min=20
max=0
Cnt=0
sum=0
nota=int(input("Indique una nota\n"))
while nota > -1:
    if nota > 20:
        while nota < -1 or nota > 20:
            print("Error (0->20, -1 salida)")
            nota=int(input())
    if nota >= 0:
        Cnt=Cnt+1
        sum=sum+nota
        if nota < min:
            min=nota
        if nota > max:
            max=nota
        nota=int(input("Indique una nota\n"))
if Cnt > 0:
    med=sum/Cnt
    print("Número de notas:",Cnt)
    print("Nota la más baja:",min)
    print("Nota la más alta:",max)
    print("Media:",med)
else:
    print("No se ha introducido ninguna nota.")
