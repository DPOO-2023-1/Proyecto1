import ply.lex as lex
import ply.yacc as yacc

tokens = [
#SIGNOS
    "INT",

    "ID",
    
    "CORCHI",

    "CORCHD",

    "DPUNTOS",

    "PCOMA",

    "COMA",
    
    "LINEA"
]

reserved = {"ROBOT_R" : "ROBOT_R",

    "VARS" : "VARS",

    "GOTO" : "GOTO",
  
    "ROBOT_R" : "ROBOT_R",

    "VARS" : "VARS",

    "VAR" : "VAR",

    "If" : "IF",

    "while" : "WHILE",

    "else" : "ELSE",

    "ASSINGTO" : "ASSINGTO",

    "MOVE" : "MOVE",

    "TURN" : "TURN",

    "FACE" : "FACE",

    "PUT" : "PUT",

    "PICK" : "PICK",

    "MOVETOTHE" : "MOVETOTHE",

    "MOVEINDIR" : "MOVEINDIR",

    "JUMPTOTHE" : "JUMPTOTHE",

    "JUMPINDIR" : "JUMPINDIR", 

    "NOP" : "NOP",

#CONDICIONALES (RETURN A BOOL)

    "bool" : "BOOL",

    "FACING" : "FACING",

    "CANPUT" : "CANPUT",

    "CANPICK" : "CANPICK",

    "CANMOVEINDIR" : "CANMOVEINDIR",

    "CANJUMPINDIR" : "CANJUMPINDIR",

    "CANMOVETOTHE" : "CANMOVETOTHE",

    "CANJUMPTOTHE" : "CAMJUMPTOTHE",

    "NOT" : "NOT"}

tokens = tokens + list(reserved.values())

#LECTURA DE TOKENS

t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value =  int(t.value)
    return t

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value,"ID") #Checar las palabras reservadas
    return t

t_CORCHI = r"\["

t_CORCHD = r"\]"

t_DPUNTOS = r"\:"

t_PCOMA = r"\;"

t_COMA = r"\,"

t_LINEA = r"\|"

''''

def t_VAR(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = "VAR"
    return t
'''''

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)




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
    