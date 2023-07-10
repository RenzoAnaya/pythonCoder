from paquete.cliente import Cliente
from paquete.menu import menu
import paquete.usuario

cliente = Cliente("John Doe", "johndoe@email.com", "123 Main St")
cliente.agregar_a_lista("Computadora")
cliente.agregar_a_lista("Celular android")
cliente.eliminar_de_lista("Celular android")
cliente.agregar_a_lista("Celular Iphone")
cliente.agregar_a_lista("Tablet")
cliente.agregar_a_lista("Audífonos")
cliente.agregar_a_lista("Cargador")
cliente.agregar_a_lista("Cable USB")
cliente.agregar_a_lista("Mouse")

print(cliente) 
print(f'Tienes {len(cliente)} objetos en tu carrito de compras')
print("Los objetos en tu carrito de compras son:")
for item in cliente:
    print(item)

menu()
