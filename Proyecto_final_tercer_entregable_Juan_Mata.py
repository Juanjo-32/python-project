import sys
import os
from time import sleep
import json


def add(inventario):
    print('Objeto a añadir')
    nombre_producto = (input('Escriba el nombre del producto: '))
    codigo_numerico = (input('Escriba el codigo numerico del producto: '))
    precio_unitario = float(input('Escriba el precio unitario del producto: '))
    cantidad = int(input('Escriba la cantidad del producto: '))
    inventario.append({'Nombre':nombre_producto, "Codigo":codigo_numerico, "Precio":precio_unitario, 'Unidad':cantidad})
    print("Articulo agregado al inventario exitosamente!")


def consultar(subinventario):
    print("Codigo:   Nombre:   Unidad:   Precio:   ")
    for producto in subinventario:
        print(str(producto['Codigo']) + '      ' + producto['Nombre'] + '     ' + str(producto['Unidad']) + '       ' + str(producto['Precio']))


def delete(subinventario):
    product_code = (input("Digite el codigo del producto a eliminar: "))
    found = 0
    for producto in subinventario:
        if product_code == producto['Codigo']:
            print("Producto existente")
            found = 1
            subinventario.remove(producto) 
            print("Su producto ha sido eliminado!")
            break
    if found == 0:
        print("El producto que trata de eliminar no existe, intente nuevamente")


def is_admin(user):
    return user['role'] == 'admin'


def is_guest(user):
    return user['role'] == 'Invitado'


def inventory_access(inventario,permiso):
    user_response = input('Desea ingresar al sistema de inventarios(si/no): ')
    if user_response == 'si':
        resp = ""
        while resp != '4':
            print('Seleccione un departamento')
            print('1- Damas')
            print('2- Caballeros')
            print('3- Niños')
            print('4- Salir')
            resp = input('Seleccione opcion: ')
            guardar = 0
            if resp == '1':
                print('Menú de productos del departamento de Damas')
                inventarios = inventario['departamentos']
                DAMAS = inventarios[0]["nombre_producto"]
                guardar = inventary(DAMAS,permiso)
            elif resp == '2':
                print('Menú de productos del departamento de Caballeros')
                inventarios = inventario['departamentos']
                CABALLEROS = inventarios[1]["nombre_producto"]
                guardar = inventary(CABALLEROS,permiso)
            elif resp == '3':
                print('Menú de productos del departamento de Niños')
                inventarios = inventario['departamentos']
                NINOS = inventarios[2]["nombre_producto"]
                guardar = inventary(NINOS,permiso)
            if guardar == 1:
                save(inventario)



def inventary(inventario,permiso):
    if permiso == 1:
        print('1-Consultar')
        print('2-Ingresar')
        print('3-Actualizar')
        print('4-Eliminar')
        print('5-Guardar')
        print('6-Volver')
        print('7-Salir')
        respuesta = input("Elija una opcion: ")
        if respuesta == '1':
            print('Consulta de productos')
            consultar(inventario)
            sleep(3)
            os.system('cls')
        elif respuesta == '2':
            print('Ingrese el producto')
            add(inventario)
            sleep(2)
            os.system('cls')
        elif respuesta == '3':
            print('Actualice el producto')
            update(inventario)
            sleep(2)
            os.system('cls')
        elif respuesta == '4':
            print('Elimine el producto')
            delete(inventario)
            sleep(2)
            os.system('cls')
        elif respuesta == '5':
            print('Guardando menu de departamentos')
            sleep(2)
            os.system('cls')
            return 1
        elif respuesta == '6':
            print('Volviendo al menu de departamentos')
            sleep(2)
            os.system('cls')
        elif respuesta == '7':
            print('Saliendo del sistema de inventarios')
            sleep(2)
            os.system('cls') 

    else:
        print('1-Consultar')
        print('2-Volver')
        print('3-Salir')
        respuesta = input("Elija una opcion: ")
        if respuesta == '1':
            print("Consulta de productos")
            consultar(inventario)
            sleep(2)
            os.system('cls')
        elif respuesta == '2':
            print('Regresando al menu de departamentos')
            sleep(2)
            os.system('cls')
        else:
            print('Saliendo del sistema de inventarios')
            sleep(2)
            os.system('cls')
    return 0


def read(archivo_inventario):
    with open(archivo_inventario, 'r') as archivo:
        return json.load(archivo)


def save(inventory_information):
    with open("inventario.json", "w") as archivo:
        archivo.write(json.dumps(inventory_information))


def update(subinventario):
    product_code = (input("Digite el codigo del producto a actualizar: "))
    found = 0
    for producto in subinventario:
        if product_code == producto['Codigo']:
            print("Producto existente")
            found = 1
            nombre_producto = (input('Escriba el nombre del producto: '))
            precio_unitario = float(input('Escriba el precio unitario del producto: '))
            cantidad = int(input('Escriba la cantidad del producto: '))
            producto.update({'Nombre':nombre_producto, "Precio":precio_unitario, 'Unidad':cantidad})
            print("Producto actualizado correctamente!")
            break          
    if found == 0:
        print("Producto no existe!")


print('       Tienda Simon       ')
print('       Juan J. Mata       ')
print('        Bienvenido        ')

users = [{
    'username': 'admin',
    'password': 'admin',
    'full_name': 'Alejandro Sanchez',
    'role': 'admin',
},{
    'username': 'guest',
    'password': 'guest',
    'full_name': 'Juan Mata',
    'role': 'Invitado',
}]


inventory_information = {
    'nombre_tienda': 'Tienda Simon Escazu',
    'sede': 'Escazu',
    'departamentos': [
        {'nombre': "Damas", 'nombre_producto': [],},
        {'nombre':'Caballeros', 'nombre_producto': [],},
        {'nombre': 'Ninos', 'nombre_producto': [],},
        ],
}

user_in = (input('Digite su usuario: '))
password_in = (input('Digite su contraseña: '))

try:
    inventario_cargado = read("inventario.json")
    inventory_information = inventario_cargado
except:
    print("Aun no existen productos en la base de datos")

logged_user = None

for user in users:
    if user['username'] == user_in and user['password'] == password_in:
        logged_user = user
        break

if not logged_user:
    print('Usuario incorrecto, saliendo del programa')
    sys.exit()

sleep(1)
os.system('cls')

print(f"Bienvenido al sistema de inventarios de tienda Simón, {logged_user['full_name']} es un place atenderle!")

if is_admin(logged_user):
    inventory_access(inventory_information,1)

if is_guest(logged_user):
    inventory_access(inventory_information,0)

print('Salio del programa')






