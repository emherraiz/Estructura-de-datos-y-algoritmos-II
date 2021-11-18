__author__ = 'febel'
import math,sys
if len(sys.argv) != 3:
    print("Son necesarios 3 argumentos")
    sys.exit(0)
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
max=-b/(2*a)
delta=(b*b)-(4*a*c)
if delta>0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    if x1>x2:
        extremo1=x2-10
        extremo2=x1+10
    else:
        extremo1=x1-10
        extremo2=x2+10
elif delta <= 0:
    extremo1=max-10
    extremo2=max+10
for x in range(int(extremo1),int(extremo2+1)):
    y=a*x*x+b*x+c
    print("f(",x,")=",y)