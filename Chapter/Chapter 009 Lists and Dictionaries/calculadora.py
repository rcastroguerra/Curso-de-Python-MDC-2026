import sys

if len(sys.argv) != 3:
    print("Uso: python calculadora.py numero1 numero2")
    sys.exit(1)

# Convertimos strings a números
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")