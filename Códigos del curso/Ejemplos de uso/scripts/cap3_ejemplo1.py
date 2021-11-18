import math
print("Indique a,b y  c")
a=int(input())
b=int(input())
c=int(input())
delta=(b*b)-(4*a*c)
if(delta > 0):
         x1=(-b+math.sqrt(delta)/(2*a))
         x2=(-b-math.sqrt(delta)/(2*a))
         print("Las dos dos soluciones son x1=",x1," x2=",x2)
elif(delta==0):
               x1=-b/(2*a)
               print("La única solución es: x1=",x1)
else:
     print("La ecuación no tiene solución")