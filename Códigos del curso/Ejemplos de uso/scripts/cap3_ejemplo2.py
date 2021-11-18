anio=int(input("indique un año\n"))
if (anio%4==0) and ((anio%400==0) or (anio%100>0)):
    print(anio," es bisiesto\n")
else:
    print(anio," no es bisiesto\n")