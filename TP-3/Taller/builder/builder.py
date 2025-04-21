from vehiculo import Vehiculo

class VehiculoBuilder:
    def __init__(self):
        self.vehiculo = Vehiculo()

    def construir_chasis(self):
        pass

    def instalar_motor(self):
        pass

    def colocar_ruedas(self):
        pass

    def pintar(self):
        pass

    def obtener_vehiculo(self):
        return self.vehiculo
 