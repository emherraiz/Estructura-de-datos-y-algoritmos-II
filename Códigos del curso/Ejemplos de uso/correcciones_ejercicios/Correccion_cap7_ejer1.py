__author__ = 'febel'
import sys
o="test"
try:
    FicSRC=open("SRC.jpg","r")
    FicDST=open("DST.jpg","rw")
except:
    print("NO exiten los archivos")
    sys.exit(0)
while o != " ":
    o=FicSRC.reda(10)
    FicDST.write(o)

FicSRC.close()
FicDST.close()
