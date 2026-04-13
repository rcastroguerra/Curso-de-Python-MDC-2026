import argparse

parser = argparse.ArgumentParser(description="Configuración del programa")

# Argumentos opcionales
parser.add_argument("--nombre", "-n", type=str, help="Nombre del usuario")
parser.add_argument("--edad", "-e", type=int, help="Edad del usuario")
parser.add_argument("--verbose", "-v", action="store_true", help="Modo verboso")

args = parser.parse_args()

if args.verbose:
    print("🔊 Modo verboso activado")

if args.nombre:
    print(f"Nombre: {args.nombre}")

if args.edad:
    print(f"Edad: {args.edad}")