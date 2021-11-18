__author__ = 'febel'
#solución 1
for n in range(1,1001):
    i=2
    while i<n and n%i>0:
        i=i+1
    if i==n:
        print(n)

#solución 2
for n in range(1,101):
    test=False
    if n==2:
        test=True
    else:
        if n%2 !=0:
            i=3
            while i<n and n%i > 0:
                i+=2
        if i==n:
            test=True
    if test:
        print(n)

#solución final
import math
for n in range(1,101):
    test=False
    if n==2:
        test=True
    else:
        if n%2 !=0:
            limite=math.sqrt(n)+1
            i=3
            while i<limite and n%i > 0:
                i+=2
        if n!=1 and i>limite:
            test=True
    if test:
        print(n)

