__author__ = 'febel'
anio=1975
mes=12
dia=3
c_dia=""
numdia=anio-(anio/100)*100
numdia=numdia+(numdia/4)
numdia=numdia+dia
if mes==10:
    numdia=numdia+1
elif mes==11:
    numdia=numdia+4
elif mes==5:
    numdia=numdia+2
elif mes==6:
    numdia=numdia+1
elif mes==8:
    numdia=numdia+6

if (anio%4==0 and anio%400==0) or anio%100>0:
    numdia=numdia-1
var=anio/100
if var==20:
    numdia=numdia+6
elif var==21:
    numdia=numdia+4
elif var==18:
    numdia=numdia+2

numdia=numdia%7
if numdia==1:
    c_dia="domingo"
elif numdia==2:
    c_dia="lunes"
elif numdia==3:
    c_dia="martes"
elif numdia==4:
    c_dia="miércoles"
elif numdia==5:
    c_dia="jueves"
elif numdia==6:
    c_dia="viernes"
elif numdia==0:
    c_dia=="sábado"

print(c_dia)

