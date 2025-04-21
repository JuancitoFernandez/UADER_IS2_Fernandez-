# Patron de diseño Singleton
from EmpresaCuit import EmpresaCUIT

if __name__ == "__main__":
    gestor_cuit = EmpresaCUIT()
    print("empreas disponibles:")
    for nombre in gestor_cuit.empresas:
        print(f" - {nombre}")

    nombre_empresa =  input("ingrese nombre de la empresa: ")

    try:
        cuit = gestor_cuit.obtener_cuit(nombre_empresa)
        print(f"CUIT de {nombre_empresa}: {cuit}")
    except ValueError as e:
        print(e)
      
