def buscar(termino):
    print(f"Buscando {termino}...")
    return ["resultado1", "resultado2"]

# Este código está en el ámbito global
print("Bienvenido a Web Search")
termino = input("Ingrese búsqueda: ")
resultado = buscar(termino)