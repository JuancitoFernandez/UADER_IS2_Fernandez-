import copy

class AvionPrototype:
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def clonar(self):
        return copy.deepcopy(self)

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}, Capacidad: {self.capacidad} pasajeros")


def main():
    # Crea el avión original
    avion_original = AvionPrototype("Boeing 737", 180)
    print("Avión original:")
    avion_original.mostrar_info()

    # clona el avion original
    clon1 = avion_original.clonar()
    print("\nClon 1:")
    clon1.mostrar_info()

    # clona a partir del clon
    clon2 = clon1.clonar()
    print("\nClon 2 (del clon 1):")
    clon2.mostrar_info()

    # verificacion
    print("\nVerificación de instancias:")
    print(f"avion_original is clon1? {avion_original is clon1}")
    print(f"clon1 is clon2? {clon1 is clon2}")


if __name__ == "__main__":
    main()
