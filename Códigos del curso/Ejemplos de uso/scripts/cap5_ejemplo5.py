p = [[None, None, None], [None, None, None], [None, None, None]]
peon = ' '
x = 0
y = 0
for i in (0, 1, 2):
    for j in (0, 1, 2):
        p[i][j] = " "
gana = False
numturnos = 0
while not gana and numturnos != 9:
    if peon != 'o':
        peon = 'o'
    else:
        peon = 'x'
    while x < 0 or x > 2 or y < 0 or y > 2 or p[x][y] != ' ':
        print("     1   2   3")
        for i in (0, 1, 2):
            print(i + 1, "|", p[i][0], "| ", p[i][1], "|", p[i][2], "| ")
        print("Es turno de ", peon)
        print("Coordenadas (x,y)?")
        x = int(input()) - 1
        y = int(input()) - 1

    p[x][y] = peon
    i = 0
    while i < 3 and not gana:
        if p[i][0] != ' ' and p[i][0] == p[i][1] and p[i][0] == p[2][i]:
            gana = True
        i = i + 1
    i = 0
    while i < 3 and not gana:
        if p[0][i] != ' ' and p[0][i] == p[1][i] and p[0][i] == p[2][i]:
            gana = True
        i = i + 1
    if (p[1][1] != ' ' and ((p[0][0] == p[1][1] and p[0][0] == p[2][2])
                            and (p[0][2] == p[1][1] and p[0][2] == p[2][0]))):
        gana = True
    numturnos = numturnos + 1
    print("numturnos:", numturnos)

print("     1   2   3")
for i in (0, 1, 2):
    print(i + 1, "| ", p[i][0], "| ", p[i][1], "| ", p[i][2], "|")
if gana:
    print(peon, " gana")
else:
    print("Nadie ha ganado")
