__author__ = 'febel'
tab=[10,17,14,3,12,2,15,9,7,10,14,13,8,1,9,19,17,14,2,5]
valor=14
num_ocurrencias=0
for i in range(0,20):
    if tab[i]==valor:
        num_ocurrencias=num_ocurrencias+1
print(num_ocurrencias)