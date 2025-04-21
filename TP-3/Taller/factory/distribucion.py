class MetodoDistribucion:
    def enviar_remito(self, remito):
        raise NotImplementedError("Debe implementar 'enviar_remito' en la subclase.")

class Correo(MetodoDistribucion):
    def enviar_remito(self, remito):
        print(f"Enviando remito por correo: {remito}")

class Mensajeria(MetodoDistribucion):
    def enviar_remito(self, remito):
        print(f"Enviando remito por mensajería: {remito}")

class PortalVentas(MetodoDistribucion):
    def enviar_remito(self, remito):
        print(f"Publicando remito en el portal de ventas: {remito}")
