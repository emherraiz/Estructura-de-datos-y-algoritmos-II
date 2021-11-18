__author__ = 'febel'
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=fact(10)
print(n)