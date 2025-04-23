# Clase base
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def calcular(self):
        return self.valor

# Decorador base
class OperacionDecorator(Numero):
    def __init__(self, numero: Numero):
        self.numero = numero

    def calcular(self):
        return self.numero.calcular()

# Decoradores concretos
class SumarDos(OperacionDecorator):
    def calcular(self):
        return self.numero.calcular() + 2

class MultiplicarPorDos(OperacionDecorator):
    def calcular(self):
        return self.numero.calcular() * 2

class DividirPorTres(OperacionDecorator):
    def calcular(self):
        return self.numero.calcular() / 3

if __name__ == "__main__":
    base = Numero(9)

    print("Valor original:", base.calcular())

    # Aplicaciones decoradas individualmente
    suma = SumarDos(base)
    print("Suma de 2:", suma.calcular())

    multiplicado = MultiplicarPorDos(base)
    print("Multiplicado por 2:", multiplicado.calcular())

    dividido = DividirPorTres(base)
    print("Dividido por 3:", dividido.calcular())

    # Invocación anidada
    anidado = DividirPorTres(MultiplicarPorDos(SumarDos(base)))
    print("((9 + 2) * 2) / 3 =", anidado.calcular())
