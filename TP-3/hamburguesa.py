# ejercicio 3
class MetodoEntrega:
    def entregar(self):
        pass

# Entregas al mostrador
class EntregaMostrador(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa será entregada en mostrador.")

class RetiroCliente(MetodoEntrega):
    def entregar(self):
        print("El cliente retirará la hamburguesa.")

class Delivery(MetodoEntrega):
    def entregar(self):
        print("La hamburguesa será enviada por delivery.")


class Hamburguesa:
    def __init__(self, metodo_entrega: MetodoEntrega):
        self.metodo_entrega = metodo_entrega

    def entregar(self):
        self.metodo_entrega.entregar()



# ejecucion del programa
hamburguesa1 = Hamburguesa(EntregaMostrador())
hamburguesa2 = Hamburguesa(RetiroCliente())
hamburguesa3 = Hamburguesa(Delivery())

hamburguesa1.entregar()  
hamburguesa2.entregar()  
hamburguesa3.entregar()  