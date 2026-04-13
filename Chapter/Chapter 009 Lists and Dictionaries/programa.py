import sys

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Falta el nombre del archivo")
        print("Uso: python programa.py archivo.txt")
        sys.exit(1)  # Código 1 = error
    
    print(f"✅ Procesando {sys.argv[1]}")
    sys.exit(0)  # Código 0 = éxito

if __name__ == "__main__":
    main()