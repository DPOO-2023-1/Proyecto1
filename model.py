import ply.lex as lex
import ply.yacc as yacc

tokens = [
#SIGNOS
    "INT",

    "NAME",
    
    "CORCHI",

    "CORCHD",

    "DPUNTOS",

    "PCOMA",

    "COMA",
    
    "LINEA"
]

reserved = {"robot_r" : "ROBOT_R",

    "vars" : "VARS",

    "procs" : "PROCS",

    "goto" : "GOTO",

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

    "facing" : "FACING",

    "canput" : "CANPUT",

    "canpick" : "CANPICK",

    "canmoveindir" : "CANMOVEINDIR",

    "canjumpindir" : "CANJUMPINDIR",

    "canmovetothe" : "CANMOVETOTHE",

    "canjumptothe" : "CANJUMPTOTHE",

    "not" : "NOT",

#extras

    "left" : "LEFT",
      
    "right" : "RIGHT",
     
    "around" : "AROUND",

    "north" : "NORTH",

    "south" : "SOUTH",

    "east" : "EAST",

    "west" : "WEST",

    "balloons" : "BALLOONS",

    "chips" : "CHIPS",

    "front" : "FRONT",

    "back" : "BACK",

    "do" : "DO",

    "repeat" : "REPEAT",

    "procedure_call" : "procedure_call",

    "control_structure": "control_structure"
    
    }

tokens = tokens + list(reserved.values())

#LECTURA DE TOKENS

t_ignore = " \t"

def t_INT(t):
    r"\d+"
    t.value =  int(t.value)
    return t

def t_NAME(t):
    r"(?i)[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value,"NAME") #Checar las palabras reservadas
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_CORCHI = r"\["

t_CORCHD = r"\]"

t_DPUNTOS = r"\:"

t_PCOMA = r"\;"

t_COMA = r"\,"

t_LINEA = r"\|"


def t_error(t):
     print("Illegal character '%s'" % t.value[0])




lexer = lex.lex()

def CARGAR_ARCHIVO(nombre : str)->str:

    archivo = open(nombre)
    linea = archivo.readline()
    texto = ""
    while linea != "":
        texto += linea
        linea = archivo.readline()

    return texto.lower()
#TODO se cambia el nombre de la función para que genere menor confusión. se quita su tipo de retorno bool.
def TOKENIZAR_CODIGO(texto : str):
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


def p_program(p):
    '''program : ROBOT_R VARS var_list PROCS proc_def instruction_block
                | ROBOT_R PROCS proc_def instruction_block
                | ROBOT_R VARS instruction_block
                | ROBOT_R instruction_block
                | ROBOT_R PROCS
                | ROBOT_R VARS
                | ROBOT_R
                | empty'''
    if len(p) == 7:
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4])
    elif len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]


def p_var_list(p):
    '''var_list : NAME var_list_tail
                | NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_var_list_tail(p):
    '''var_list_tail : COMA NAME var_list_tail PCOMA
                     | COMA NAME PCOMA'''
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[3]

def p_proc_def(p):
    '''proc_def : NAME CORCHI parameters CORCHD instruction_block
                | NAME CORCHI parameters CORCHD instruction_block proc_def '''
    
    if len(p) == 6:
        p[0] = [('procedure', p[1], p[3], p[5])]
    else:
        p[0] = [('procedure', p[1], p[3], p[5])] + p[6]

def p_parameters(p):
    '''parameters : LINEA NAME parameters_tail LINEA
                  | LINEA NAME LINEA
    '''

    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[3]

def p_parameters_tail(p):
    '''parameters_tail : COMA NAME parameters_tail
                       | COMA NAME
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_instruction_block(p):
    '''instruction_block : CORCHI instructions CORCHD
                         | CORCHI CORCHD
    '''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]

def p_instructions(p):
    '''instructions : instruction instructions
                    | instruction
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

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
                  | NOP
                  | procedure_call
                  | control_structure
    '''
    p[0] = p[1]

def p_assignTo(p):
    '''assignTo : ASSINGTO PCOMA NAME COMA INT'''
    p[0] = ( p[1], p[2], p[3], p[4], p[5])

def p_goto(p):
    '''goto : GOTO DPUNTOS INT COMA INT'''
    p[0] = ( p[1], p[2] ,p[3], p[4], p[5])

def p_move(p):
    '''move : MOVE DPUNTOS INT'''
    p[0] = (p[1], p[2], p[3])

def p_turn(p):
    '''turn : TURN DPUNTOS LEFT
           | TURN DPUNTOS RIGHT
           | TURN DPUNTOS AROUND
    '''
    p[0] = (p[1], p[2], p[3])


def p_face(p):
    '''face : FACE DPUNTOS NORTH
           | FACE DPUNTOS SOUTH
           | FACE DPUNTOS EAST
           | FACE DPUNTOS WEST
    '''
    p[0] =  (p[1], p[2], p[3])

def p_put(p):
    '''put : PUT DPUNTOS INT COMA BALLOONS
          | PUT DPUNTOS INT COMA CHIPS
    '''
    p[0] = ( p[1], p[2], p[3] ,p[4], p[5])

def p_pick(p):
    '''pick : PICK DPUNTOS INT COMA BALLOONS
           | PICK DPUNTOS INT COMA CHIPS
    '''
    p[0] = ( p[1], p[2], p[3], p[4], p[5])

def p_moveToThe(p):
    '''moveToThe : MOVETOTHE DPUNTOS INT COMA FRONT
                | MOVETOTHE DPUNTOS INT COMA LEFT
                | MOVETOTHE DPUNTOS INT COMA RIGHT
                | MOVETOTHE DPUNTOS INT COMA BACK
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_moveInDir(p):
    '''moveInDir : MOVEINDIR DPUNTOS INT COMA NORTH
                 | MOVEINDIR DPUNTOS INT COMA SOUTH
                 | MOVEINDIR DPUNTOS INT COMA EAST
                 | MOVEINDIR DPUNTOS INT COMA WEST
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_jumpToThe(p):
    '''jumpToThe : JUMPTOTHE DPUNTOS INT COMA FRONT
                | JUMPTOTHE DPUNTOS INT COMA LEFT
                | JUMPTOTHE DPUNTOS INT COMA RIGHT
                | JUMPTOTHE DPUNTOS INT COMA BACK
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_jumpInDir(p):
    '''jumpInDir : JUMPINDIR DPUNTOS INT COMA NORTH
                 | JUMPINDIR DPUNTOS INT COMA SOUTH
                 | JUMPINDIR DPUNTOS INT COMA EAST
                 | JUMPINDIR DPUNTOS INT COMA WEST
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5])

def p_proccall(p):
    'instruction : NAME DPUNTOS args'
    p[0] = ('proccall', p[1], p[3])

def p_controlstructure(p):
    '''instruction : IF DPUNTOS condition THEN DPUNTOS instructions ELSE DPUNTOS instructions
                   | WHILE DPUNTOS condition DO DPUNTOS instructions
                   | REPEAT DPUNTOS args DPUNTOS instructions'''
    if p[1] == 'if':
        p[0] = ('if', p[3], p[6], p[9])
    elif p[1] == 'while':
        p[0] = ('while', p[3], p[6])
    else:
        p[0] = ('repeat', p[3], p[6])

def p_condition(p):
    '''condition : FACING NAME
                 | CANPUT args COMA NAME
                 | CANPICK args COMA NAME
                 | CANMOVEINDIR args COMA NAME
                 | CANJUMPINDIR args COMA NAME
                 | CANMOVETOTHE args COMA NAME
                 | CANJUMPTOTHE args COMA NAME
                 | NOT condition'''
    if p[1] == 'facing':
        p[0] = ('facing', p[2])
    elif p[1] == 'canput':
        p[0] = ('canput', p[2], p[4])
    elif p[1] == 'canpick':
        p[0] = ('canpick', p[2], p[4])
    elif p[1] == 'canmoveindir':
        p[0] = ('canmoveindir', p[2], p[4])
    elif p[1] == 'canjumpindir':
        p[0] = ('canjumpindir', p[2], p[4])
    elif p[1] == 'canmovetothe':
        p[0] = ('canmovetothe', p[2], p[4])
    elif p[1] == 'canjumptothe':
        p[0] = ('canjumptothe', p[2], p[4])
    else:
        p[0] = ('not', p[2])

def p_args(p):
    '''args : arg
            | arg COMA args'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_arg(p):
    '''arg : NAME
           | INT'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in line %d" % p.lineno)

def p_empty(p):
    '''

    empty : 

    '''
    p[0] = None

#TODO Se elimina el tipo de parametro que recibe la función del parser.
parser = yacc.yacc()

def parse_code(code_tokenizado):

    result = parser.parse(code_tokenizado)

    return result
    

