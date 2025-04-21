from builder import VehiculoBuilder

class AutoBuilder(VehiculoBuilder):
    def __init__(self):
        super().__init__()
        self.vehiculo.tipo = "Auto"

    def construir_chasis(self):
        self.vehiculo.chasis = "Chasis auto estándar"

    def instalar_motor(self):
        self.vehiculo.motor = "Motor 1.6L"

    def colocar_ruedas(self):
        self.vehiculo.ruedas = "4 ruedas de aleación"

    def pintar(self):
        self.vehiculo.color = "Rojo"

class MotoBuilder(VehiculoBuilder):
    def __init__(self):
        super().__init__()
        self.vehiculo.tipo = "Moto"

    def construir_chasis(self):
        self.vehiculo.chasis = "Chasis ligero"

    def instalar_motor(self):
        self.vehiculo.motor = "Motor 250cc"

    def colocar_ruedas(self):
        self.vehiculo.ruedas = "2 ruedas deportivas"

    def pintar(self):
        self.vehiculo.color = "Negro"
