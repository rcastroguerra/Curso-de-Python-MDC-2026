import argparse

parser = argparse.ArgumentParser(description="Calculadora")

parser.add_argument("--operacion", "-o", 
                    choices=["suma", "resta", "multiplica", "divide"],
                    default="suma",
                    help="Operación a realizar")
parser.add_argument("numeros", nargs="+", type=float, help="Números a operar")

args = parser.parse_args()

if args.operacion == "suma":
    resultado = sum(args.numeros)
elif args.operacion == "resta":
    resultado = args.numeros[0] - sum(args.numeros[1:]) if len(args.numeros) > 1 else args.numeros[0]
elif args.operacion == "multiplica":
    resultado = 1
    for n in args.numeros:
        resultado *= n
elif args.operacion == "divide":
    resultado = args.numeros[0]
    for n in args.numeros[1:]:
        resultado /= n

print(f"Resultado: {resultado}")