# Clase base del patrón Composite
class Componente:
    def mostrar(self, nivel=0):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clase hoja
class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")

# Clase compuesta
class Conjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Conjunto: {self.nombre}")
        for comp in self.componentes:
            comp.mostrar(nivel + 1)

# Crear el producto principal
producto = Conjunto("Producto Principal")

# Crear 3 subconjuntos principales
for i in range(1, 4):
    subconjunto = Conjunto(f"Subconjunto {i}")
    for j in range(1, 5):
        subconjunto.agregar(Pieza(f"Pieza {i}.{j}"))
    producto.agregar(subconjunto)

# Mostrar estructura inicial
print("== Estructura inicial del ensamblado ==")
producto.mostrar()

# Agregar subconjunto opcional
sub_opcional = Conjunto("Subconjunto Opcional")
for k in range(1, 5):
    sub_opcional.agregar(Pieza(f"Pieza O.{k}"))
producto.agregar(sub_opcional)

# Mostrar estructura final
print("\n== Estructura con subconjunto adicional ==")
producto.mostrar()
