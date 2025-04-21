from concrete_builders import AutoBuilder, MotoBuilder
from director import DirectorVehiculo

def elegir_builder(tipo):
    if tipo.lower() == "auto":
        return AutoBuilder()
    elif tipo.lower() == "moto":
        return MotoBuilder()
    else:
        raise ValueError("Tipo de vehículo no soportado.")

if __name__ == "__main__":
    tipo = input("¿Qué vehículo desea construir? (auto/moto): ")

    try:
        builder = elegir_builder(tipo)
        director = DirectorVehiculo(builder)
        vehiculo = director.construir_vehiculo()
        print("\nVehículo construido con éxito:")
        vehiculo.mostrar()
    except ValueError as e:
        print(f"Error: {e}")
