def main():
    print("nombre del modulo:", __name__ )
    print("Este codigo se ejecuta solo si corres el archivo directamente")
    print("se esta ejecutando el if __name__ == '__main__'")

if __name__ == "__main__":
    main()

else:
    print("Ejecutando", __name__,".py como modulo")