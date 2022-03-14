from nodo import nodo
class ListaCola():
    def __init__(self):
        self.ultimo:nodo = None
        self.primero:nodo= None
        self.size=0

    def insertar(self, nombre, nit, dire, ingre, tiempo):
        nuevo = nodo(nombre, nit, dire, ingre, tiempo)
        self.size +=1
        if self.ultimo==None:
            self.ultimo = nuevo
            self.primero= nuevo
        else:
            nuevo.setSiguiente(self.ultimo)
            self.ultimo.setAnterior(nuevo)
            self.ultimo = nuevo
  

    def imprimir(self):
        if self.size>0:
            tmp=self.ultimo
            for x in range(self.size):
                print(tmp.getNombre())
                tmp=tmp.getSiguiente()
        else:
            print("No se encuentran ordenes pendientes")

    def eliminar(self):
        if self.size>0:
            newClient=self.primero.getNombre()
            if self.size==1:
                self.ultimo=None
                self.primero=None
                self.size-=1
            else:
                previous=self.primero.getAnterior()
                previous.setSiguiente(None)
                self.primero=previous
                self.size-=1
            print("Se despacho la orden "+newClient)
        else:
            print("No se encuentran ordenes pendientes")