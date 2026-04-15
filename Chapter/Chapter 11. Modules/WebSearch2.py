# WebSearch.py (versión corregida)
def buscar(termino):
    print(f"Buscando {termino}...")
    return ["resultado1", "resultado2"]

# El código dentro de este if SOLO se ejecuta si el archivo es un script
if __name__ == "__main__":
    print("Bienvenido a Web Search")
    termino = input("Ingrese búsqueda: ")
    resultado = buscar(termino)