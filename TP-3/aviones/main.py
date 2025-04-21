

class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con:")
        for parte in self.partes:
            print(f"- {parte}")

class AvionBuilder:
    def construir_body(self):
        pass

    def construir_turbinas(self):
        pass

    def construir_alas(self):
        pass

    def construir_tren_aterrizaje(self):
        pass

    def obtener_avion(self):
        pass

class AvionComercialBuilder(AvionBuilder):
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("Body de avión comercial")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion

class Director:
    def __init__(self, builder: AvionBuilder):
        self.builder = builder

    def construir_avion(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren_aterrizaje()

# Ejecucion del programa

def main():
    builder = AvionComercialBuilder()
    director = Director(builder)

    director.construir_avion()
    avion_final = builder.obtener_avion()
    avion_final.mostrar()

if __name__ == "__main__":
    main()
