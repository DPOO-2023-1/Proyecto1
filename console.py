import controller

def CARGARMENU():

    opcion = "1"

    while opcion[0] != "2":
        print("""BIENVENIDO AL EVALUADOR DE CODIGO
        
        1. Evaluar tu archivo de codigo 
        2. Salir de la aplicacion\n""")

        opcion = input("¿Que desea hacer?: ")

        if opcion[0] == "1":
            EVALUARCODIGO()
        elif opcion[0] == "2":
            print("Se cerró el programa con exito\n")
        else:
            print("Ingrese una opcion valida\n")


def EVALUARCODIGO ():
    
    nombre = input("Ingrese el nombre del archivo: ")

    if nombre == "":
        print("Ingrese un nombre")
    
    texto = controller.CARGAR_ARCHIVO(nombre)
    texto_tokenizado = controller.TOKENIZARCODIGO(texto)
    rta = controller.parse_code(texto)

    print(rta)

    if rta == None:
        print("="*50)  
        print("El codigo no sirve")
        print("="*50)
    else:
        print("="*50)  
        print("¡El codigo sí sirve!")
        print("="*50)
    #TODO Se comento el return texto, ya que no se sentía pertinente. 
    #return texto
    
CARGARMENU()

