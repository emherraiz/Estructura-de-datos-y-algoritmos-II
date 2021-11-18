__author__ = 'febel'
def convert_to_hexa(n):
    hexa=""
    while n!=0:
        resto=n%16
        if resto <=9:
            resto=resto+48
        else:
            resto=resto+87
        hexa=str(hex(resto)+hexa)
        n=n//16

def Formato(campo, longitud,car,derecho):
    long=len(campo)
    numcar=longitud-long
    while(numcar != 0):
        if derecho:
            campo=campo+car
        else:
            campo=car+campo
        numcar=numcar-1
    return campo

long=16
o="a"
contador=0
sContador=""
hexlist=""
carlist="|"
FicSRC=open("SRC.jpg","r")
pos=0

while o != " ":
    o=FicSRC.read(1)
    print(o)
    pos=pos+1
    if pos%long==0 and pos !=0:
        print("en pos !=0")
        sContador=Formato(convert_to_hexa(contador),8,'0',False)
        print(sContador,"     ",hexlist," ",carlist,"|")
        contador=pos
        hexlist=""
        carlist="|"
    if o != " ":
        print(o)
        hexlist=hexlist+Formato(convert_to_hexa(o),2,'0',False)
        if o > 31 and o < 127:
            carlist=carlist+str(o)
        else:
            carlist=carlist+"."
    sContador=Formato(convert_to_hexa(contador),8,'0',False)
    if len(hexlist)<3*long:
        hexlist=Formato(hexlist,3*long,' ',True)
    print(sContador,"     ",hexlist," ",carlist,"|")
FicSRC.close()

