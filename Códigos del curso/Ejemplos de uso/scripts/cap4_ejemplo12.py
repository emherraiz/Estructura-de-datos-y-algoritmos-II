__author__ = 'febel'
x=1
a=31
cont=5
while x*x < a:
    x=x+1
if x*x != a:
    x=x-1
    for i in range(1,cont+1):
        x=0.5*(x+(a/x))
print(x)
print(x**2)