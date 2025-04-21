# Ejercicio 4
class Factura:
    def __init__(self, importe):
        self.importe = importe

    def mostrar_detalle(self):
        pass


class FacturaIVAResponsable(Factura):
    def mostrar_detalle(self):
        print(f"Factura A - IVA Responsable Inscripto - Total: ${self.importe:.2f}")

class FacturaIVANoInscripto(Factura):
    def mostrar_detalle(self):
        print(f"Factura C - IVA No Inscripto - Total: ${self.importe:.2f}")

class FacturaIVAExento(Factura):
    def mostrar_detalle(self):
        print(f"Factura E - IVA Exento - Total: ${self.importe:.2f}")

# fabrica de facturas
class FacturaFactory:
    @staticmethod
    def crear_factura(condicion_impositiva, importe):
        if condicion_impositiva == "IVA Responsable":
            return FacturaIVAResponsable(importe)
        elif condicion_impositiva == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion_impositiva == "IVA Exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condición impositiva no válida.")


# ejecucion del programa

factura1 = FacturaFactory.crear_factura("IVA Responsable", 1000)
factura2 = FacturaFactory.crear_factura("IVA No Inscripto", 800)
factura3 = FacturaFactory.crear_factura("IVA Exento", 500)

factura1.mostrar_detalle()  # Factura A - IVA Responsable Inscripto 
factura2.mostrar_detalle()  # Factura C - IVA No Inscripto 
factura3.mostrar_detalle()  # Factura E - IVA Exento 
