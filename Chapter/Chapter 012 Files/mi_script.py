import sys
import os

# 🔍 Mostrar información de argumentos
print("Todos los argumentos:", sys.argv)
print("Número de argumentos:", len(sys.argv))
print("Nombre del script:", sys.argv[0])

print("-" * 40)

# Verificar que el usuario haya escrito exactamente 1 argumento
# (más el nombre del script, que es sys.argv[0])
# Verificar que el archivo existe
if not os.path.exists(sys.argv[1]):
    print("El archivo no existe.")
    sys.exit(1)  # 1 indica error

# 📄 Obtener archivo desde argumento
archivo = sys.argv[1]
print(f"Abriendo archivo: {archivo}")

# 📖 Leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)