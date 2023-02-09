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

reserved = {"robot_r" : "ROBOT_R",

    "vars" : "VARS",

    "goto" : "GOTO",

    "var" : "VAR",

    "if" : "IF",

    "while" : "WHILE",

    "else" : "ELSE",

    "then" : "THEN",

    "assingto" : "ASSINGTO",

    "move" : "MOVE",

    "turn" : "TURN",

    "face" : "FACE",

    "put" : "PUT",

    "pick" : "PICK",

    "movetothe" : "MOVETOTHE",

    "moveindir" : "MOVEINDIR",

    "jumtothe" : "JUMPTOTHE",

    "jumpindir" : "JUMPINDIR", 

    "nop" : "NOP",

#CONDICIONALES (RETURN A BOOL)

    "bool" : "BOOL",

    "facing" : "FACING",

    "canput" : "CANPUT",

    "canpick" : "CANPICK",

    "canmoveindir" : "CANMOVEINDIR",

    "canjumpindir" : "CANJUMPINDIR",

    "canmovetothe" : "CANMOVETOTHE",

    "canjumptothe" : "CAMJUMPTOTHE",

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
    r"[a-zA-Z_][a-zA-Z_0-9]*" #PENDIENTE REVISIÓN
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

    return texto.lower()

def EVALUAR_CODIGO(texto : str)->bool:
    lexer.input(texto)
    tokenized = []
    while True:
        tok = lexer.token()
        tokenized.append(tok)
        if not tok:
            break
        

    return tokenized
    
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

    program : ROBOT_R VARS
 

    '''
    p[0] = p[1]             #pendiente de revisión

def p_vars(p): #Modificacion sebas

    '''
    VARS : ID PCOMA PROCS
            | vars_list PCOMA PROCS
            
    '''
    p[0] = (p[1], p[2], p[3])

def p_id_pcoma(p):

    '''
    
    var_list : ID COMA vars_list


    '''

    p[0] = (p[1], p[2], p[3])

def p_final_vars_list(p):
    '''
    
    var_list : ID

    '''
    p[0] = p[1]

def p_procs(p): #Declaracion de funciones
    '''
    
    procs : PROCS procedure_def procs
             | PROCS procedure_def
             
    '''
    if len(p) == 4:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = [p[2]]

def p_procedure_def(p):
    '''

    procedure_def : ID "(" parameters ")" block
    
    '''
    p[0] = ('procedure_def', p[1], p[3], p[5])

def p_parameters(p):
    '''
    
    parameters : ID "," parameters
                 | ID
                 
    '''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_conditional(p): #Declaracion condicionales
    '''

    conditional : IF condition THEN instructions ELSE instructions
                   | IF condition THEN instructions
                   
    '''
    if len(p) == 6:
        p[0] = ('if', p[2], p[4], p[6])
    else:
        p[0] = ('if', p[2], p[4])

def p_loop(p):
    'loop : WHILE condition DO instructions'
    p[0] = ('while', p[2], p[4])

def p_repeat(p):
    'repeat : REPEAT number TIMES instructions'
    p[0] = ('repeat', p[2], p[4])

def p_condition(p):
    '''condition : FACING direction
                 | CANPUT number X
                 | CANPICK number X
                 | CANMOVEINDIR number direction
                 | CANJUMPINDIR number direction
                 | CANMOVETOTHE number direction
                 | CANJUMPTOTHE number direction
                 | NOT condition'''
    if p[1] == 'not':
        p[0] = ('not', p[2])
    else:
        p[0] = (p[1], p[2], p[3])

def p_block_instructions(p):
    'block_instructions : LBRACKET instruction_list RBRACKET'
    p[0] = p[2]

def p_instruction_list(p):
    '''instruction_list : instruction_list SEMICOLON instruction
                        | instruction'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_instruction(p):
    '''instruction : assignTo
                  | goto
                  | move
                  | turn
                  | face
                  | put
                  | pick
                  | moveToThe
                  | moveInDir
                  | jumpToThe
                  | jumpInDir
                  | nop
                  | procedure_call
                  | control_structure'''
    p[0] = p[1]

    

def p_empty(p):
    '''

    empty : 

    '''
    p[0] = None

parser = yacc.yacc

