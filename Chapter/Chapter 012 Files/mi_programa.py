import sys

# ❌ sys.argv[0] = nombre del programa (NO lo escribes tú)
# ❌ sys.argv[1] = PRIMER ARGUMENTO que tú pasas desde la terminal

if len(sys.argv) != 2:
    print(f"Uso: python {sys.argv[0]} mi_archivo.txt")
    sys.exit(1)

archivo = sys.argv[1]   # ⭐ ESTE ES EL ARGUMENTO REAL
print(f"Abriendo archivo: {archivo}")

with open(archivo, 'r', encoding='utf-8') as f:
    contenido = f.read()
    print(contenido)