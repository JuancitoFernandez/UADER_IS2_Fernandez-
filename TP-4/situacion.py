# Flyweight
class FlyweightArbol:
    def __init__(self, tipo, textura, color, forma_tronco):
        self.tipo = tipo
        self.textura = textura
        self.color = color
        self.forma_tronco = forma_tronco

    def mostrar(self, x, y):
        print(f"{self.tipo} en posición ({x}, {y}) con textura {self.textura}, color {self.color}, tronco {self.forma_tronco}")

# Flyweight Factory
class FabricaDeArboles:
    _flyweights = {}

    @staticmethod
    def obtener_arbol(tipo):
        if tipo not in FabricaDeArboles._flyweights:
            if tipo == "Pino":
                FabricaDeArboles._flyweights[tipo] = FlyweightArbol("Pino", "rugosa", "verde", "fino")
            elif tipo == "Roble":
                FabricaDeArboles._flyweights[tipo] = FlyweightArbol("Roble", "áspera", "marrón", "grueso")
            elif tipo == "Abeto":
                FabricaDeArboles._flyweights[tipo] = FlyweightArbol("Abeto", "suave", "verde oscuro", "mediano")
            else:
                raise ValueError("Tipo de árbol no reconocido.")
        return FabricaDeArboles._flyweights[tipo]

# Árbol individual (estado extrínseco)
class Arbol:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.flyweight = FabricaDeArboles.obtener_arbol(tipo)

    def mostrar(self):
        self.flyweight.mostrar(self.x, self.y)

# Bosque que contiene muchos árboles
class Bosque:
    def __init__(self):
        self.arboles = []

    def plantar_arbol(self, x, y, tipo):
        arbol = Arbol(x, y, tipo)
        self.arboles.append(arbol)

    def mostrar_bosque(self):
        for arbol in self.arboles:
            arbol.mostrar()

if __name__ == "__main__":
    bosque = Bosque()

    # Plantamos varios árboles
    bosque.plantar_arbol(10, 20, "Pino")
    bosque.plantar_arbol(15, 25, "Pino")
    bosque.plantar_arbol(5, 8, "Roble")
    bosque.plantar_arbol(12, 18, "Abeto")
    bosque.plantar_arbol(7, 3, "Abeto")

    print("\n🌳 Árboles en el bosque:")
    bosque.mostrar_bosque()
