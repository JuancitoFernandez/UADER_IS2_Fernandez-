# Implementador
class TrenLaminador:
    def producir(self, lamina):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Implementaciones concretas
class Tren5Metros(TrenLaminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor}\" x {lamina.ancho}m x 5m de largo en Tren de 5 metros.")

class Tren10Metros(TrenLaminador):
    def producir(self, lamina):
        print(f"Produciendo lámina de {lamina.espesor}\" x {lamina.ancho}m x 10m de largo en Tren de 10 metros.")

# Abstracción
class Lamina:
    def __init__(self, tren_laminador: TrenLaminador):
        self.espesor = 0.5       # en pulgadas
        self.ancho = 1.5         # en metros
        self.tren = tren_laminador

    def producir(self):
        self.tren.producir(self)

if __name__ == "__main__":
    tren5 = Tren5Metros()
    tren10 = Tren10Metros()

    lamina1 = Lamina(tren5)
    lamina2 = Lamina(tren10)

    lamina1.producir()
    lamina2.producir()
