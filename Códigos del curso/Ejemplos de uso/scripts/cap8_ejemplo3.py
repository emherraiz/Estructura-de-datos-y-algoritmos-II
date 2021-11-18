__author__ = 'febel'
class tfabricante():
    nombre=""
    direccion=""
    telefono=""
class tarticulo():
    ref=""
    etiqueta=""
    precio=0.0
    fab=tfabricante

articulo=tarticulo
articulo.ref="Art001_01"
articulo.fab=tfabricante
articulo.fab.ref="Fab1234"
art2=articulo
print(art2.ref)
print(art2.fab.ref)
