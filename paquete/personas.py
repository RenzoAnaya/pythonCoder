class Persona:
    def __init__(self, nombre, email, ruta):
        self.nombre = nombre
        self.email = email
        self.ruta = ruta

    def __str__(self):
        return f'Nombre: {self.nombre}, Email: {self.email}'


class Usuario(Persona):
    def __init__(self, nombre, email, ruta):
        super().__init__(nombre, email, ruta)

    def reiniciar(self):
        with open(self.ruta, "w") as f:
            input("Presione ENTER para reiniciar los registros")
    
    def registro(self):
        with open(self.ruta, "a") as f:
            print("Registre un nuevo usuario")
            nombre = input("Ingrese su nombre: ").strip()
            email = input("Ingrese su correo: ").strip()
            contrasena = input("Ingrese una contraseña: ").strip()
            if email and contrasena:
                f.write(f"email: {email}, contrasena: {contrasena}, nombre: {nombre}\n")
                print("Usuario registrado con éxito")
            else:
                print("Correo o contraseña no válidos")

    def ver_usuarios(self):
        with open(self.ruta, "r") as f:
            print(f.read())

    def login(self):
        email = input("Ingrese su correo: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()
        with open(self.ruta, "r") as f:
            lineas = f.readlines()
            usuario_valido = False
            for linea in lineas:
                datos = linea.strip().split(",")
                email_registrado = datos[0].split(":")[1].strip()
                contrasena_registrada = datos[1].split(":")[1].strip()
                if email == email_registrado and contrasena == contrasena_registrada:
                    usuario_valido = True
                    break
            if usuario_valido:
                print("Sesión iniciada.")
            else:
                print("Su correo o contraseña no coinciden con nuestros registros.")






class Cliente(Persona):
    def __init__(self, nombre, email, ruta):
        super().__init__(nombre, email, ruta)
        self.lista_compras = []

    def agregar_a_lista(self, item):
        self.lista_compras.append(item)
        
    def eliminar_de_lista(self, item):
        if item in self.lista_compras:
            self.lista_compras.remove(item)
        
    def __len__(self):
        return len(self.lista_compras)
    
    def __iter__(self):
        return iter(self.lista_compras)
