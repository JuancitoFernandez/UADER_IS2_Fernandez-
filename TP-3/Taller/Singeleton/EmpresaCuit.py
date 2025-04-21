# empresa_cuit.py
from Singleton import SingletonMeta

class EmpresaCUIT(metaclass=SingletonMeta):
    def __init__(self):
        # Simulación de una base de datos de empresas
        self.empresas = {
            "Netflix": "30-12345678-9",
            "Samsumg": "30-87654321-0",
            "Iphone": "30-11112222-3",
            "acer": "30-78569243-7"
        }

    def obtener_cuit(self, nombre_empresa):
        cuit = self.empresas.get(nombre_empresa)
        if cuit:
            return cuit
        else:
            raise ValueError(f"No se encontró CUIT para la empresa '{nombre_empresa}'")
