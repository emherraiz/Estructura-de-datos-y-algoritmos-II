__author__ = 'febel'

def par(n):
    if n==0:
        return True
    else:
        return impar(n-1)

def impar(n):
    if n==0:
        return False
    else:
        return par(n-1)
