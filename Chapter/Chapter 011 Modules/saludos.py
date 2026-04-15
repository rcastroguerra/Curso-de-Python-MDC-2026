def hola():
    print("Hola desde el módulo!")

def adios():
    print("Adiós desde el módulo!")

# Solo se ejecuta si este archivo es el script principal
if __name__ == "__main__":
    print("=== Probando el módulo ===")
    hola()
    adios()
    print("=== Fin de la prueba ===")