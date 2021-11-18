__author__ = 'febel'
print("indique x y n")
n=1
signo=False
x=int(input())
n=int(input())
if n < 0:
    n=-n
    signo=True
cont=1
resultado=1
while cont <= n:
    resultado=resultado*x
    cont=cont+1
if signo:
    resultado=(1/resultado)
print(resultado)