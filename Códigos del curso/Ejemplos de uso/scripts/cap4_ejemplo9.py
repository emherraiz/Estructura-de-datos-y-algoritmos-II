__author__ = 'febel'
a=1
while a <= 100:
    b=1
    while b <= 100:
        c=1
        while c <= 100:
            num1=a*100+b*10+c
            num2=a**3+b**3+c**3
            if num1==num2:
                print(a," ",b," ",c)
            c=c+1
        b=b+1
    a=a+1