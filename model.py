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

def t_NAME(t):
    r"(?i)[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value,"NAME") #Checar las palabras reservadas
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

def p_program(p):
    '''program : ROBOT_R VARS var_list
               | ROBOT_R PROCS proc_def
               | ROBOT_R instruction_block'''
    if len(p) == 5:
        if p[2] == 'VARS':
            p[0] = ('declaration', p[3])
        elif p[2] == 'PROCS':
            p[0] = ('procedure_declaration', p[3])
    else:
        p[0] = ('instruction_block', p[3])

def p_var_list(p):
    '''var_list : NAME var_list_tail
                | NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_var_list_tail(p):
    '''var_list_tail : COMMA NAME var_list_tail
                     | COMMA NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_proc_def(p):
    '''proc_def : NAME LBRACKET parameters RBRACKET instruction_block
                | NAME LBRACKET parameters RBRACKET instruction_block proc_def'''
    if len(p) == 6:
        p[0] = [('procedure', p[1], p[3], p[5])]
    else:
        p[0] = [('procedure', p[1], p[3], p[5])] + p[6]

def p_parameters(p):
    '''parameters : PIPE NAME parameters_tail PIPE
                  | PIPE NAME PIPE'''
    if len(p) == 4:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[3]

def p_parameters_tail(p):
    '''parameters_tail : COMMA NAME parameters_tail
                       | COMMA NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_instruction_block(p):
    '''instruction_block : LBRACKET instructions RBRACKET
                         | LBRACKET RBRACKET'''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]

def p_instructions(p):
    '''instructions : instruction instructions
                    | instruction'''
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
                  | nop
                  | procedure_call
                  | control_structure
    '''
    p[0] = p[1]

def p_assignTo(p):
    '''assignTo : NAME ',' INT'''
    p[0] = ('assignTo', p[1], p[3])

def p_goto(p):
    '''goto : INT ',' INT'''
    p[0] = ('goto', p[1], p[3])

def p_move(p):
    '''move : INT'''
    p[0] = ('move', p[1])

def p_turn(p):
    '''turn : LEFT
           | RIGHT
           | AROUND
    '''
    p[0] = ('turn', p[1])

def p_face(p):
    '''face : NORTH
           | SOUTH
           | EAST
           | WEST
    '''
    p[0] = ('face', p[1])

def p_put(p):
    '''put : INT ',' BALLOONS
          | INT ',' CHIPS
    '''
    p[0] = ('put', p[1], p[3])

def p_pick(p):
    '''pick : INT ',' BALLOONS
           | INT ',' CHIPS
    '''
    p[0] = ('pick', p[1], p[3])

def p_moveToThe(p):
    '''moveToThe : INT ',' FRONT
                | INT ',' LEFT
                | INT ',' RIGHT
                | INT ',' BACK
    '''
    p[0] = ('moveToThe', p[1], p[3])

def p_moveInDir(p):
    '''moveInDir : INT ',' NORTH
                 | INT ',' SOUTH
                 | INT ',' EAST
                 | INT ',' WEST
    '''
    p[0] = ('moveInDir', p[1], p[3])

def p_jumpToThe(p):
    '''jumpToThe : INT ',' FRONT
                | INT ',' LEFT
                | INT ',' RIGHT
                | INT ',' BACK
    '''
    p[0] = ('jumpToThe', p[1], p[3])

def p_jumpInDir(p):
    '''jumpInDir : INT ',' NORTH
                 | INT ',' SOUTH
                 | INT ',' EAST
                 | INT ',' WEST
    '''
    p[0] = ('jumpInDir', p[1], p[3])

def p_nop(p):
    'instruction : NOP'
    p[0] = ('nop',)

def p_proccall(p):
    'instruction : NAME COLON args'
    p[0] = ('proccall', p[1], p[3])

def p_controlstructure(p):
    '''instruction : IF COLON condition THEN COLON instructions ELSE COLON instructions
                   | WHILE COLON condition DO COLON instructions
                   | REPEAT COLON args COLON instructions'''
    if p[1] == 'if':
        p[0] = ('if', p[3], p[6], p[9])
    elif p[1] == 'while':
        p[0] = ('while', p[3], p[6])
    else:
        p[0] = ('repeat', p[3], p[6])

def p_condition(p):
    '''condition : FACING NAME
                 | CANPUT args COMMA NAME
                 | CANPICK args COMMA NAME
                 | CANMOVEINDIR args COMMA NAME
                 | CANJUMPINDIR args COMMA NAME
                 | CANMOVETOTHE args COMMA NAME
                 | CANJUMPTOTHE args COMMA NAME
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
            | arg COMMA args'''
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

parser = yacc.yacc()

def parse_code(code : str):

    result = parser.parse(code)

    return result
    

