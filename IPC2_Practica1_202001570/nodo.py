class nodo():
    def __init__(self,nombre, nit, dire, ingre, tiempo):
        self.nombre = nombre
        self.nit = nit
        self.dire = dire
        self.ingre = ingre
        self.tiempo = tiempo
        self.siguiente=None
        self.anterior=None

    def getSiguiente(self):
        return self.siguiente

    def getAnterior(self):
        return self.anterior

    def getNombre(self):
        return self.nombre
    
    def getNit(self):
        return self.nit

    def getDire(self):
        return self.dire
    
    def getIngre(self):
        return self.ingre

    def getTiempo(self):
        return self.tiempo

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setNit(self, nit):
        self.nit = nit

    def setDire(self, dire):
        self.dire = dire

    def setIngre(self, ingre):
        self.ingre = ingre

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setAnterior(self, anterior):
        self.anterior = anterior
    