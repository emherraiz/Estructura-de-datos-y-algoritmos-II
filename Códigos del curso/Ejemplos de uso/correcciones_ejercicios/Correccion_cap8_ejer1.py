__author__ = 'febel'
class nodo:
    pIzquierdo=None
    pDerecho=None

def infijo(rNodo):
    if rNodo != None:
        infijo(rNodo.pIzquierdo)
        print(rNodo.valor)
        infijo(rNodo.pDerecho)
