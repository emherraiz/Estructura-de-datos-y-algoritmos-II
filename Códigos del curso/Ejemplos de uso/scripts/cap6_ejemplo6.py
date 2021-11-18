__author__ = 'febel'


def ordenar_tabla(tab):
    Cnt = len(tab)
    for i in range(1, Cnt):
        mem = tab[i]
        pos = i - 1
        while pos >= 0 and tab[pos] > mem:
            tab[pos + 1] = tab[pos]
            pos = pos - 1
        tab[pos + 1] = mem


t = [48, 17, 25, 9, 34]
Cnt = len(t)
print("Antes:")
for i in range(0, Cnt):
    print(t[i], " ", end=" ")
ordenar_tabla(t)
print("Después:")
for i in range(0, Cnt):
    print(t[i], " ", end=" ")
print("")
