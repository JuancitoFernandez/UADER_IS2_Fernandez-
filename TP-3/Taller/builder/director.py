class DirectorVehiculo:
    def __init__(self, builder):
        self.builder = builder

    def construir_vehiculo(self):
        self.builder.construir_chasis()
        self.builder.instalar_motor()
        self.builder.colocar_ruedas()
        self.builder.pintar()
        return self.builder.obtener_vehiculo()
