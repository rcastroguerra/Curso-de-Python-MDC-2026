import sys

# Verificamos que haya exactamente 3 argumentos (programa + nombre + edad)
if len(sys.argv) != 3:
    print("❌ Error: Número incorrecto de argumentos")
    print("Uso: python saludo_seguro.py nombre edad")
    sys.exit(1)  # Salimos del programa con código de error 1

# Si llegamos aquí, hay argumentos suficientes
nombre = sys.argv[1]
edad = int(sys.argv[2])

print(f"Hola {nombre}.")
print(f"{edad} es una gran edad.")