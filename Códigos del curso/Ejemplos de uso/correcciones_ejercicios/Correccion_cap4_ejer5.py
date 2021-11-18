__author__ = 'febel'
n=12456
binario=""
while n != 0:
    if n%2==0:
        binario="0"+binario
    else:
        binario="1"+binario
    n=n//2
print(binario)