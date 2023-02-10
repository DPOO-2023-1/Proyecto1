import model

def CARGAR_ARCHIVO(nombre : str)->str:
    texto = model.CARGAR_ARCHIVO(nombre)
    return texto
#TODO Se elimina el tipo de parametro que entrega el codigo, ya que no tiene sentido que sea un bool.
def TOKENIZARCODIGO(codigo):
    tokens = model.TOKENIZAR_CODIGO(codigo)
    #print(tokens) Se comenta este print para que no se impriman los tokens en la respuesta.
    return tokens
#TODO Se elimina el tipo de parametro que recibe el parser para probar su funcionamiento.  
def parse_code(codigo_tokenizado):
    return model.parse_code(codigo_tokenizado)