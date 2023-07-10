class Cliente:
    def __init__(self, nombre, email, direccion_envio):
        self.nombre = nombre
        self.email = email
        self.direccion_envio = direccion_envio
        self.lista_compras = []
        
    def agregar_a_lista(self, item):
        self.lista_compras.append(item)
        
    def eliminar_de_lista(self, item):
        if item in self.lista_compras:
            self.lista_compras.remove(item)
        
    def __str__(self):
        return f'Cliente: {self.nombre}, Email: {self.email}'
    
    def __len__(self):
        return len(self.lista_compras)
    
    def __iter__(self):
        for pos in range(len(self.lista_compras)):
            yield f'El obejto número {pos+1} es {self.lista_compras[pos]}'