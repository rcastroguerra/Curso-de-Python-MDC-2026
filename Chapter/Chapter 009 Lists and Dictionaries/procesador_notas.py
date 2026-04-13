import sys

def main():
    # Verificamos argumentos
    if len(sys.argv) < 2:
        print("❌ Uso incorrecto")
        print("Uso: python procesador_notas.py nota1 nota2 nota3 ...")
        print("Ejemplo: python procesador_notas.py 85 90 78 92")
        sys.exit(1)
    
    # Los argumentos son sys.argv[1], sys.argv[2], etc.
    # Necesitamos al menos una nota
    if len(sys.argv) < 2:
        print("❌ Error: Debes ingresar al menos una nota")
        sys.exit(1)
    
    # Convertimos las notas a números (excepto el índice 0)
    notas = []
    for i in range(1, len(sys.argv)):
        try:
            nota = float(sys.argv[i])
            notas.append(nota)
        except ValueError:
            print(f"❌ Error: '{sys.argv[i]}' no es un número válido")
            sys.exit(1)
    
    # Procesamos las notas
    total = sum(notas)
    promedio = total / len(notas)
    max_nota = max(notas)
    min_nota = min(notas)
    
    print("\n📊 RESULTADOS")
    print("=" * 30)
    print(f"Notas ingresadas: {notas}")
    print(f"Cantidad de notas: {len(notas)}")
    print(f"Total: {total}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {max_nota}")
    print(f"Nota más baja: {min_nota}")

if __name__ == "__main__":
    main()