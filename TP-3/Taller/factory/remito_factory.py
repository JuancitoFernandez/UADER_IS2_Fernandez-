from Factory import DistribucionFactory
from distribucion import Correo, Mensajeria, PortalVentas

class RemitoFactory(DistribucionFactory):
    def crear_metodo(self, tipo):
        tipo = tipo.lower()
        if tipo == "correo":
            return Correo()
        elif tipo == "mensajeria":
            return Mensajeria()
        elif tipo == "portal":
            return PortalVentas()
        else:
            raise ValueError(f"Tipo de distribución desconocido: '{tipo}'")
