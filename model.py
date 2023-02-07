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

    "goto" : "GOTO",

    "VAR" : "VAR",

    "If" : "IF",

    "while" : "WHILE",

    "else" : "ELSE",

    "then" : "THEN",

    "assingTo" : "ASSINGTO",

    "move" : "MOVE",

    "turn" : "TURN",

    "face" : "FACE",

    "put" : "PUT",

    "pick" : "PICK",

    "moveToThe" : "MOVETOTHE",

    "moveInDir" : "MOVEINDIR",

    "jumToThe" : "JUMPTOTHE",

    "jumpInDir" : "JUMPINDIR", 

    "nop" : "NOP",

#CONDICIONALES (RETURN A BOOL)

    "bool" : "BOOL",

    "facing" : "FACING",

    "canPut" : "CANPUT",

    "canPick" : "CANPICK",

    "canMoveInDir" : "CANMOVEINDIR",

    "canJumpInDir" : "CANJUMPINDIR",

    "canMoveToThe" : "CANMOVETOTHE",

    "CanJumpToThe" : "CAMJUMPTOTHE",

    "not" : "NOT"}

tokens = tokens + list(reserved.values())

#LECTURA DE TOKENS

t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value =  int(t.value)
    return t

def t_ID(t):
    r"(?i)[a-zA-Z_][a-zA-Z_0-9]*"
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
    

'''

=====================================================

--------------------Parsing--------------------------

=====================================================

'''

def p_robot(p):
    '''

    robot : program 
            | empty

    '''
    print(p[1])

def p_program(p):
    '''

    program : ROBOT_R VARS varsset
 

    '''
    p[0] = p[1]             #pendiente de revisión

def p_varsset(p):

    '''
    varsset : ID COMA ID
            
    '''
    p[0] = (p[2], p[1], p[3])

def p_varsset_end(p):

    '''
    varsset : ID PCOMA PROCS procedure
            
    '''
    p[0] = p[1]             #Pendiente de revisión

def p_procedure_definition(p):
    '''
    procedure : ID CORCHI procdec CORCHD
            
    '''
def p_procedure_recursive(p):
    '''
    procedure : procedure procedure 
    '''

    

def p_empty(p):
    '''

    empty : 

    '''
    p[0] = None
