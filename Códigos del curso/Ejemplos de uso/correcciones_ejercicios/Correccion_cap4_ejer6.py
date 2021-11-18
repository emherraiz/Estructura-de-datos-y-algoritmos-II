__author__ = 'febel'
n=123456
hexa=""
while n != 0:
    resto=n%16
    if resto >= 0 and resto <=9:
        hexa=str(resto)+hexa
    else:
        if resto == 10:
            hexa="A"+hexa
        elif resto== 11:
            hexa="B"+hexa
        elif resto==12:
            hexa="C"+hexa
        elif resto==13:
            hexa="D"+hexa
        elif resto==14:
            hexa="E"+hexa
        elif resto==15:
            hexa="F"+hexa
    n=n//16
print(hexa)

n=123456
print(hex(n))