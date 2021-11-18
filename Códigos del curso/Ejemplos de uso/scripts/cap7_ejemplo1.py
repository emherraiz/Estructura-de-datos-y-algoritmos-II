__author__ = 'febel'
def recolle(fragmento,separador):
    cadena=""
    l=len(fragmento)
    for i in range(0,l):
        cadena=cadena+morceau[i]
        if i!=(l-1):
            cadena=cadena+separador
    return cadena

cont=0
passwd=""
linea="x"
try:
    archivo=open("/etc/passwd", "r")
except:
    print("archivo ausente")

while(linea != " "):
    linea=archivo.readlinea()
    if linea!=" ":
        passwd[cont]=linea.split(":v")
        cont=cont+1
    FicSort="micopia"
    cont=0
    while passwd[cont]!=" ":
        linea=recolle(passwd[cont],":")
        FicSort.write(linea,"\n")
        cont=cont+1
FicSort.close()
archivo.close()

