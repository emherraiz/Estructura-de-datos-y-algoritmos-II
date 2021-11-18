__author__ = 'febel'
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            num1=a*100+b*10+c
            num2=a**3+b**3+c**3
            if num1==num2:
                print(num1," " ,a," ",b," ",c)



