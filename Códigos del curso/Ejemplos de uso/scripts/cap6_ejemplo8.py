__author__ = 'febel'
def deplace(n,a,b,c):
    if n>0:
        deplace(n-1,a,c,b)
        print("De ",a," a ",b)
        deplace(n-1,c,b,a)

deplace(3,1,2,3)