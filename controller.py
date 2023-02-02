import model

def CARGAR_ARCHIVO(nombre : str)->str:
    texto = model.CARGAR_ARCHIVO(nombre)
    return texto

def EVALUARCODIGO(codigo: str)->bool:
    return model.EVALUAR_CODIGO(codigo)