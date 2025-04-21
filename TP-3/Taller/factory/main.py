from remito_factory import RemitoFactory

if __name__ == "__main__":
    remito = "Remito N°0001 - Cliente: Juan Pérez - Producto: Laptop"

    print("Métodos disponibles: correo, mensajeria, portal")
    tipo = input("Ingrese el tipo de distribución: ")

    try:
        factory = RemitoFactory()
        metodo = factory.crear_metodo(tipo)
        metodo.enviar_remito(remito)
    except ValueError as e:
        print(e)
