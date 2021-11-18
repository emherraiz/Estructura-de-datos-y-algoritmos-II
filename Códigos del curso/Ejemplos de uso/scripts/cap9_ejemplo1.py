__author__ = 'febel'


class Pantalla:
    global num_pantallas
    num_pantallas = 0

    def __init__(self, t="Desconocido", mg="Desconocido", mdl="Desconocido"):
        print("constructor por defecto o  3 argumentos")
        self.type = t
        self.marca = mg
        self.modelo = mdl
        self.num_pantallas = num_pantallas + 1

    def modif_tipo(self, mod):
        tmod = ["CRT", "LCD", "PLASMA"]
        ok = False
        for i in range(0, len(tmod)):
            if mod == tmod[i]:
                ok = True

    def muestra_tipo(self):
        print("tipo: ", self.type)

    def numPantallas(self):
        print("nombre pantallas (funcion):", num_pantallas)


if __name__ == '__main__':
    o1 = Pantalla("LCD", "LG", "L19155")
    o1.muestra_tipo()
    Pantalla.numPantallas(1)
    print("nombre pantalla (main):", o1.num_pantallas)
