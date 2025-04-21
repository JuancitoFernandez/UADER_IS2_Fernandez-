# Ejercicio 1
class FactorialSingleton:

    _instancia = None  # atributo de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(FactorialSingleton, cls).__new__(cls)
        return cls._instancia

    def calcular_factorial(self, numero):
        if numero < 0:
            raise ValueError("El número debe ser no negativo")
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

factorial1 = FactorialSingleton()

print(factorial1.calcular_factorial(4))