import ply.lex as lex
import ply.yacc as yacc

tokensa = [
    "ROBOT_R",

    "INT",

    "VARS",

    "VAR",

    "IF",

    "WHILE",

    "ELSE",

    "ASSINGTO",

    "MOVE",

    "TURN",

    "FACE",

    "PUT",

    "PICK",

    "MOVETOTHE",

    "MOVEINDIR",

    "JUMPTOTHE",

    "JUMPINDIR",

    "NOP",

#CONDICIONALES (RETURN A BOOL)

    "BOOL",

    "FACING",

    "CANPUT",

    "CANPICK",

    "CANMOVEINDIR",

    "CANJUMPINDIR",

    "CANMOVETOTHE",

    "CANJUMPTOTHE",

    "NOT",

#SIGNOS

    "CORCHI",

    "CORCHD",

    "DPOINT",

    "PCOMA",

    "COMA",
    
    "LINEA",

    "ID"
    
]

reserved = {"ROBOT_R" : "ROBOT_R",

    "VARS" : "VARS",

    "GOTO" : "GOTO",
  
    }



#LECTURA DE TOKENS

t_CORCHI = r"\["

t_CORCHD = r"\]"

t_DPOINT = r"\:"

t_PCOMA = r"\;"

t_COMA = r"\,"

t_LINEA = r"\|"

t_ignore = " \t"

tokens = tokensa + list(reserved.values())

def t_INT(t):
    r"\d+"
    t.value =  int(t.value)
    return t

def t_VAR(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = "VAR"
    return t

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value,"ID") #Checar las palabras reservadas
    return t

lexer = lex.lex()

def CARGAR_ARCHIVO(nombre : str)->str:

    archivo = open(nombre)
    linea = archivo.readline()
    texto = ""
    while linea != "":
        texto += linea.replace("\n"," ")
        linea = archivo.readline()

    return texto

def EVALUAR_CODIGO(texto : str)->bool:
    lexer.input(texto)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    return True
    