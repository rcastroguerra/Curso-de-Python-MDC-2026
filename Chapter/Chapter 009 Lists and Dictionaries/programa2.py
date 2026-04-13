import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Saluda al usuario")

# Agregar argumentos posicionales (obligatorios)
parser.add_argument("nombre", help="Nombre del usuario")
parser.add_argument("edad", type=int, help="Edad del usuario")

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
print(f"Hola {args.nombre}")
print(f"Tienes {args.edad} años")