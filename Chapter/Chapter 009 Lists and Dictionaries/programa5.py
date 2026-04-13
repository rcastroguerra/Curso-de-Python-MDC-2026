import sys
import getopt

def main():
    try:
        # Opciones cortas: "ho:v" (h sin argumento, o: con argumento, v sin argumento)
        # Opciones largas: ["help", "output=", "verbose"]
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output=", "verbose"])
    except getopt.GetoptError as err:
        print(f"❌ Error: {err}")
        print("Uso: python programa.py -o <archivo> [-h] [-v]")
        sys.exit(2)
    
    output_file = None
    verbose = False
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Uso: python programa.py -o <archivo> [-h] [-v]")
            sys.exit(0)
        elif opt in ("-o", "--output"):
            output_file = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
    
    print(f"Archivo de salida: {output_file}")
    print(f"Modo verboso: {verbose}")

if __name__ == "__main__":
    main()