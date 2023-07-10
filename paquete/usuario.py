class Usuario:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def reiniciar(self):
        with open(self.ruta , "w") as f:
            input("Presione ENTER para reiniciar los registros")
    
    def registro(self):
        with open(self.ruta , "a") as f:
            print("Registre un nuevo usuario")
            usuario = input("Ingrese nombre de usuario: ").strip()
            contrasena = input("Ingrese una contraseña: ").strip()
            if usuario and contrasena:
                f.write(f"usuario: {usuario}, contrasena: {contrasena}\n")
                print("Usuario registrado con éxito")
            else:
                print("Usuario o contraseña no válidos")

    def ver_usuarios(self):
        with open(self.ruta, "r") as f:
            print(f.read())

    def login(self):
        usuario = input("Ingrese su nombre de usuario: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()
        with open(self.ruta , "r") as f:
            lineas = f.readlines()
            usuario_valido = False
            for linea in lineas:
                datos = linea.strip().split(",")
                usuario_registrado = datos[0].split(":")[1].strip()
                contrasena_registrada = datos[1].split(":")[1].strip()
                if usuario == usuario_registrado and contrasena == contrasena_registrada:
                    usuario_valido = True
                    break
            if usuario_valido:
                print("Sesión iniciada.")
            else:
                print("Su nombre de usuario o contraseña no coinciden con nuestros registros.")



