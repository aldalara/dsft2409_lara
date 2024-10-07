# Menu biblioteca.
def menu_biblioteca():
    '''
    Muestra el menú de opciones de la biblioteca
    '''
    accion = input('Elige una opción:\n'
                '1. Imprimir biblioteca\n'
                '2. Buscar libro por título\n'
                '3. Añadir un libro\n'
                '4. Eliminar un libro\n'
                '5. Salir de la biblioteca')
    return accion

# Funcion 1. Imprimir biblioteca.
from biblioteca import *

def imprimir_biblioteca(): 
    for i, libro in enumerate(biblioteca):
        print(f"Título:{libro}[titulo], Autor:{libro}[autor], Año:{libro}[año]")

imprimir_biblioteca()

# Funcion 2. Buscar libro.

def buscar_libro():
    titulo_buscado = input("Escribe el título del libro que quieres buscar: ")
    
    encontrado = False  

    for i, libro in enumerate(biblioteca):
        if libro["titulo"].lower() == titulo_buscado.lower():
            print(f"{i + 1}. El libro '{libro['titulo']}' ha sido encontrado.\n Autor: {libro['autor']} \n Año: {libro['año']}")
            encontrado = True
            break 
    
    if not encontrado:
        print("Este título no se encuentra en la biblioteca. Vuelve a introducir el título.")

buscar_libro()

# Funcion 3. Añadir libro.

def añadir_libro():

    new_title = input('Introduce el título del libro que quieres añadir')
    new_author = input('introduce el autor del libro que quieres añadir')
    
    try:
        new_year = int(input('Introduce el año de publicación del nuevo libro que quieres añadir'))

    except Exception:
        print('El año debe ser un número. Se introducirá el valor por defecto 0')
        año = 0
    new_book = {'título': new_title,
        'autor': new_author,
        'año': new_year}
    
    biblioteca.append(new_book)
    print('Añadido a la biblioteca el libro', new_title)
    pprint.pprint(biblioteca)

# Funcion 4. Borrar libro.

def borrar_por_autor():
    
    autor_borrar = input('elige un autor para borrar su libro')
    libros_del_autor = 0

    for i in range(len(biblioteca)):

        if biblioteca[i]['autor'].lower() == autor_borrar.lower():
            libro_borrar = biblioteca[i]
            indice_borrar = i
            libros_del_autor = libros_del_autor + 1

    if libros_del_autor == 0:
        print('No se ha encontrado ningún libro del autor', autor_borrar)

    elif libros_del_autor == 1:
        print(f'Del autor {autor_borrar} se ha encontrado el siguiente libro:')
        print(libro_borrar)
        confirm_borrar = input(f"¿Seguro que quieres borrar el libro {libro_borrar['título']}?(Sí/No)")
        
        if confirm_borrar.lower() in ['sí', 'si']:
            biblioteca.pop(indice_borrar)
            print('Libro borrado')
            pprint.pprint(biblioteca)
       
        else:
            print('Acción cancelada. No se borrará ningún libro')
    
    else:
        print('Se encontraron varios libros de ese autor en la biblioteca. Busca por título')
        title_search = input("Escribe el título del libro que quieres borrar")
        encontrado = False
        
        for i in range(len(biblioteca)):
           
            if biblioteca[i]['título'].lower() == title_search.lower():
                encontrado = True
                print('Título encontrado')
                print(biblioteca[i])
                indice_borrar = i
                conf_borrar = input(f'¿Desea borrar el libro {title_search} ?(Sí/No)')
               
                if conf_borrar.lower() in ['sí', 'si']:
                    biblioteca.pop(indice_borrar)
                    print('Libro borrado')
                    pprint.pprint(biblioteca)
               
                else:
                    print('Acción cancelada. No se borrará ningún libro')

        if encontrado == False:
            print('No se ha encontrado ningún libro con ese título')

