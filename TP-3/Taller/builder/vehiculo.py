class Vehiculo:
    def __init__(self):
        self.tipo = None
        self.chasis = None
        self.motor = None
        self.ruedas = None
        self.color = None

    def mostrar(self):
        print(f"Vehículo: {self.tipo}")
        print(f"  Chasis: {self.chasis}")
        print(f"  Motor: {self.motor}")
        print(f"  Ruedas: {self.ruedas}")
        print(f"  Color: {self.color}")
