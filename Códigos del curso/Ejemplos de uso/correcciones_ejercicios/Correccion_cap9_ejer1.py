__author__ = 'febel'
class Libro(object):
    def __init__(self):
        self.titulo=""
        self.autor=""
        self.editor=""
        self.numpaginas=0
        self.anio=0

    def libro(self,titulo,autor,editor,numpaginas,anio):
        self.titulo=titulo
        self.autor=autor
        self.editor=editor
        self.numpaginas=numpaginas
        self.anio=anio

    def settitulo(self,titulo):
        self.titulo=titulo
    def setautor(self,autor):
        self.autor=autor
    def seteditor(self,editor):
        self.editor=editor
    def setnumpaginas(self,numpaginas):
        self.numpaginas=numpaginas
    def setanio(self,anio):
        self.anio=anio

    def gettitulo(self):
        return self.titulo
    def getautor(self):
        return self.autor
    def geteditor(self):
        return self.editor
    def getnumpaginas(self):
        return self.numpaginas
    def getanio(self):
        return self.anio

l=Libro()
print(tipo(l))
l.settitulo("Algoritmia - Técnicas fundamentales de programación")
l.setautor("Sébastien ROHAUT y  Franck EBEL")
l.seteditor("Ediciones ENI")
l.setnumpaginas(379)
l.setanio(2014)

print(l.gettitulo())
print(l.getautor())
print(l.geteditor())
print(l.getnumpaginas())
print(l.getanio())