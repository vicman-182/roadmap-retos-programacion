'''
03 ESTRUCTURAS DE DATOS
Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24
'''

''' * EJERCICIO: '''

'''
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''

''' *** Listas *** '''

# Declarar una lista
mi_lista = [1,2,3,4,5,6]

# Acceder a un elemento por indice
primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1]

# Insertar un elemento al final de la lista.
mi_lista.append(2)
print(mi_lista)

# Modificar un elemento
mi_lista[2] = 8
print(mi_lista)

# Borrar el ultimpo elemento de una lista
mi_lista.append("Este elemento sera borrado") # Añadimos un elemento al final de la lista para borrarlo en las siguientes lineas del codigo
print(mi_lista)

mi_lista.pop()
print(mi_lista)

# Ordenar los datos de la lista usando el metodo sort()

mi_lista.sort()
print(mi_lista,"Los elementos de la lista fueron ordenados de menor a mayor")


''' *** Tuplas *** '''
# Declara una tupla
mi_tupla = ("Gato","Perro","Loro")

# Acceder a los elemento de la tupla por su indice
primer_elemento = mi_tupla[0]
ultimo_elemento = mi_lista[-1]

# Las tuplas son inmutables, mo pueden modificar sus elementos

# Borrar por completo una tupla
del(mi_tupla)

''' *** Sets *** '''
# Crear un conjunto vacío
mi_conjunto = set()

# Crear un conjunto con algunos elementos
mi_conjunto = {1, 2, 3, 'Python', True}

# Agregar un elemento al conjunto
mi_conjunto.add(4)

# Remover un elemento del conjunto
mi_conjunto.remove(2)

# Comprobar si un elemento está en el conjunto
existe = 'Python' in mi_conjunto  # True

''' *** Diccionarios *** '''
# Crear un diccionario vacío
mi_diccionario = {}
print(type(mi_diccionario))

# Crear un diccionario con algunos pares clave-valor
mi_diccionario = {
    'nombre': 'Victor',
    'apellido': 'Hernandez',
    'edad': 28,
    'lenguaje': 'Python'
}
print(mi_diccionario)
# Acceder a un valor por su clave
nombre = mi_diccionario['nombre']  # 'Victor'

# Modificar un valor
mi_diccionario['edad'] = 29

# Agregar un nuevo par clave-valor
mi_diccionario['ciudad'] = 'Maturin'

# Ordenar un diccionario
dic_order = dict(sorted(mi_diccionario.items()))
print(dic_order)

'''
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
*   los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
*/
'''

def mi_agenda():
    
    agenda = {}

    while True:
        print("\n --- Agenda de Contactos --- ")
        print("   1. Buscar Contacto")
        print("   2. Ingresar Contacto")
        print("   3. Actualizar Contacto")
        print("   4. Eliminar Contacto")
        print("   5. Salir")
        print(" --------------------------- ")
    
        opcion = input("\nSelecciona una opcion: ")
        
        match opcion:
            case "1": 
                pass
            case "2":
                nombre = input("\nIngrese el nombre: ")
                numero = input("\nIngrese el numero: ")
                if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
                    mi_agenda[nombre] = numero
                else:
                    print("Debes de introducir un numero que tenga maximo 11 digitos")
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Usted ha salido del programa")
                break
            case _:
                print("\nOpcion no valida, ingrese una opcion del 1-5")

mi_agenda()

