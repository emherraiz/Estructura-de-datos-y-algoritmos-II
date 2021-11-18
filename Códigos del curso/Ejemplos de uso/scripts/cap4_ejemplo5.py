__author__ = 'febel'
nota=int(input("Indique una nota\n"))
while nota > -1:
    if nota > 20:
        while nota<-1 or nota > 20:
            print("Error (0->20, -1 salida):")
            nota=int(input())
    if (nota > -1):
        nota=int(input("Indique una nota\n"))
