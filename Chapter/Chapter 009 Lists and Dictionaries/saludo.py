import sys

# Los argumentos comienzan en índice 1
nombre = sys.argv[1]
edad = int(sys.argv[2])  # Convertimos a entero

print(f"Hola {nombre}.")
print(f"{edad} es una gran edad.")