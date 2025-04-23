import subprocess

class Ping:
    def __init__(self):
        pass

    def execute(self, direccion_ip):
        if not direccion_ip.startswith("192."):
            raise ValueError("La dirección IP no es válida. Debe comenzar con '192.'")
        self._realizar_ping(direccion_ip)

    def executefree(self, direccion_ip):
        self._realizar_ping(direccion_ip)

    def _realizar_ping(self, direccion_ip):
        print(f"Realizando ping a {direccion_ip}...")
        try:
            resultado = subprocess.run(
                ["ping", "-c", "10", direccion_ip],
                capture_output=True,
                text=True
            )
            print(resultado.stdout)
            if resultado.returncode == 0:
                print("Ping exitoso.")
            else:
                print("No se pudo alcanzar la dirección IP.")
        except Exception as e:
            print(f"Ocurrió un error al ejecutar el ping: {e}")

class PingProxy:
    def __init__(self):
        self.ping_real = Ping()

    def execute(self, direccion_ip):
        if direccion_ip == "192.168.0.254":
            print("Redireccionando ping a www.google.com (modo libre)")
            self.ping_real.executefree("www.google.com")
        else:
            self.ping_real.execute(direccion_ip)

if __name__ == "__main__":
    proxy = PingProxy()

    print("Caso 1: IP válida '192.168.1.1'")
    proxy.execute("192.168.1.1")  # Realiza ping real

    print("\nCaso 2: Dirección proxy especial '192.168.0.254'")
    proxy.execute("192.168.0.254")  # Redirige a Google

    print("\nCaso 3: IP inválida '10.0.0.1'")
    try:
        proxy.execute("10.0.0.1")  # Lanza excepción
    except ValueError as e:
        print(f"Excepción atrapada: {e}")
