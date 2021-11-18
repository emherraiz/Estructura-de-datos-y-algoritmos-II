__author__ = 'febel'
cont=100000000
a=1
for i in range(2,cont+1):
    a=a+1/(i*i)
a=a*6
x=1
cont=10
while x*x < a :
    x=x+1
if x*x != a:
    x=x-1
    for i in range(1,cont+1):
        x=0.5*(x+(a/x))
print(x)