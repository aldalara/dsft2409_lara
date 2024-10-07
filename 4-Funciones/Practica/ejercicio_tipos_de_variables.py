
# Primero es mejor crear las funciones

def funcion_prueba_1():
    global biblioteca #Para que la coja
    a = 1 #Variables locales a la función prueba
    b = 2
    c = 3
    print(a,b,c)

def funcion_prueba_2():
    funcion_prueba_3()

def funcion_prueba_3():
    print("Hola")

"-----------------------"

# Luego poner las variables globales
biblioteca = {} # Variable global (está fuera de la función)

"-----------------------"

funcion_prueba_1()
#funcion_prueba_3()
funcion_prueba_2()


