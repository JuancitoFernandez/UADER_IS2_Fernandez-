# 

class CalculadoraImpuestos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instancia

    def calcular_total_impuestos(self, base_imponible):
        if base_imponible < 0:
            raise ValueError("La base imponible debe ser un valor no negativo")
        
        iva = base_imponible * 0.21         # IVA 
        iibb = base_imponible * 0.05        # IIBB 
        contribuciones = base_imponible * 0.012  # Contribuciones municipales
        
        total_impuestos = iva + iibb + contribuciones
        return total_impuestos


# Ejecucion del programa 
impuestos1 = CalculadoraImpuestos()

base = 1000 # modificar este numero para saber el numero de impuesto
total = impuestos1.calcular_total_impuestos(base)
print(f"Total de impuestos para ${base}: ${total:.2f}")



