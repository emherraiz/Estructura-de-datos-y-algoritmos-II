__author__ = 'febel'


def RepiteCar(numcar, c):
    for i in range(1, numcar + 1):
        print(c, end=" ")
    print(" ")


for num in range(1, 11):
    RepiteCar(num, '*')
