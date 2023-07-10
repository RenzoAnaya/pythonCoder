

def menu(user):

  while True:
    print("Bienvenido al Menú. Escribe el número de la opción que deseas usar")
    print("1. Registrarme")
    print("2. Borrar registros")
    print("3. Ver usuarios")
    print("4. Iniciar sesión")
    print("5. Salir")

    opcion = input("Ingrese una opción")

    if opcion == "1":
      user.registro()
    elif opcion == "2":
      user.reiniciar()
    elif opcion == "3":
      user.ver_usuarios()
    elif opcion == "4":
      user.login()
    elif opcion == "5":
      break
    else:
        print("Ingrese una opción válida")

  print("Vuelva pronto")


if __name__ == "__main__":
    menu()