import model

def CARGAR_ARCHIVO(nombre : str)->str:
    texto = model.CARGAR_ARCHIVO(nombre)
    return texto

def EVALUARCODIGO(codigo: str)->bool:
    tokens = model.EVALUAR_CODIGO(codigo)
    print(tokens)
    return tokens