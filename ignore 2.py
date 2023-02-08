import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NAME', 'NUMBER',
    'VARS', 'PROCS',
    'ASSIGNTO', 'GOTO', 'MOVE', 'TURN', 'FACE', 'PUT', 'PICK', 'MOVETOTHE', 'MOVEINDIR', 'JUMPTOTHE', 'JUMPINDIR', 'NOP',
    'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'REPEATTIMES',
    'FACING', 'CANPUT', 'CANPICK', 'CANMOVEINDIR', 'CANJUMPINDIR', 'CANMOVETOTHE', 'CANJUMPTOTHE', 'NOT',
    'NORTH', 'SOUTH', 'EAST', 'WEST', 'FRONT', 'RIGHT', 'LEFT', 'BACK',
    'BALLOONS', 'CHIPS'
)

t_NAME = r'[a-zA-Z][a-zA-Z0-9]*'
t_NUMBER = r'\d+'

t_ignore = " \t\r\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ASSIGNTO(t):
    r'assignTo:'
    return t

def t_GOTO(t):
    r'goto:'
    return t

def t_MOVE(t):
    r'move:'
    return t

def t_TURN(t):
    r'turn:'
    return t

def t_FACE(t):
    r'face:'
    return t

def t_PUT(t):
    r'put:'
    return t

def t_PICK(t):
    r'pick:'
    return t

def t_MOVETOTHE(t):
    r'moveToThe:'
    return t

def t_MOVEINDIR(t):
    r'moveInDir:'
    return t

def t_JUMPTOTHE(t):
    r'jumpToThe:'
    return t

def t_JUMPINDIR(t):
    r'jumpInDir:'
    return t

def t_NOP(t):
    r'nop'
    return t

def t_VARS(t):
    r'VARS'
    return t

def t_PROCS(t):
    r'PROCS'
    return t

def t_IF(t):
    r'if:'
    return t

def t_THEN(t):
    r'then:'
    return t

def t_ELSE(t):
    r'else:'
    return t

def t_WHILE(t):
    r'while:'
    return t

def t_DO(t):
    r'do:'
    return t

def t_REPEATTIMES(t):
    r'repeat:'
    return t

# Define the grammar
def p_program(p):
    'program : ROBOT R declaration_vars definition_procs block_instructions'
    p[0] = ("program", p[3], p[4], p[5])

def p_declaration_vars(p):
    '''declaration_vars : VARS names_list
                        | empty'''
    if len(p) == 2:
        p[0] = ("declaration_vars", [])
    else:
        p[0] = ("declaration_vars", p[2])

def p_names_list(p):
    '''names_list : NAME
                  | names_list COMMA NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_definition_procs(p):
    '''definition_procs : PROCS proc_def
                        | empty'''
    if len(p) == 2:
        p[0] = ("definition_procs", [])
    else:
        p[0] = ("definition_procs", p[2])

def p_proc_def(p):
    'proc_def : NAME LBRACKET parameters instructions RBRACKET'
    p[0] = ("proc_def", p[1], p[3], p[4])

def p_parameters(p):
    '''parameters : NAME
                  | parameters VBAR NAME COMMA parameters
                  | parameters VBAR NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 5:
        p[0] = p[1] + [p[3]] + p[5]
    else:
        p[0] = p[1] + [p[3]]

def p_block_instructions(p):
    'block_instructions : LBRACKET instructions RBRACKET'
    p[0] = ("block_instructions", p[2])

def p_instructions(p):
    '''instructions : instruction
                    | instructions SEMICOLON instruction'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_instruction(p):
    '''instruction : cmd
                   | proc_call
                   | control_structure'''
    p[0] = ("instruction", p[1])

def p_cmd(p):
    '''cmd : assign_to
           | goto
           | move
           | turn
           | face
           | put
           | pick
           | move_to_the
           | move_in_dir
           | jump_to_the
           | jump_in_dir
           | nop'''
    p[0] = ("cmd", p[1])

def p_assign_to(p):
    x = "ssign"#Incompleto toca revisar
    return None

#Inicia otra rta
def p_block(p):
    'block : LBRACKET instructions RBRACKET'
    p[0] = ('block', p[2])

def p_instructions(p):
    '''instructions : instruction
                   | instructions SEMICOLON instruction'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_instruction(p):
    '''instruction : command
                  | procedure_call
                  | control_structure'''
    p[0] = p[1]

def p_command(p):
    '''command : assignTo
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
              | nop'''
    p[0] = p[1]

def p_assignTo(p):
    'assignTo : ASSIGNTO NAME COMMA NUMBER'
    p[0] = ('assignTo', p[2], p[4])

def p_goto(p):
    'goto : GOTO NAME COMMA NAME'
    p[0] = ('goto', p[2], p[4])

def p_move(p):
    'move : MOVE NAME'
    p[0] = ('move', p[2])

def p_turn(p):
    'turn : TURN DIRECTION'
    p[0] = ('turn', p[2])

def p_face(p):
    'face : FACE ORIENTATION'
    p[0] = ('face', p[2])

def p_put(p):
    'put : PUT NAME COMMA ITEM'
    p[0] = ('put', p[2], p[4])

def p_pick(p):
    'pick : PICK NAME COMMA ITEM'
    p[0] = ('pick', p[2], p[4])

def p_moveToThe(p):
    'moveToThe : MOVE_TO_THE NAME COMMA POSITION'
    p[0] = ('moveToThe', p[2], p[4])

def p_moveInDir(p):
    'moveInDir : MOVE_IN_DIR NAME COMMA ORIENTATION'
    p[0] = ('moveInDir', p[2], p[4])

def p_jumpToThe(p):
    'jumpToThe : JUMP_TO_THE NAME COMMA POSITION'
    p[0] = ('jumpToThe', p[2], p[4])

def p_jumpInDir(p):
    'jumpInDir : JUMP_IN_DIR NAME COMMA ORIENTATION'
    p[0] = ('jumpInDir', p[2], p[4])

def p_nop(p):
    'nop : NOP'
    p[0] = ('nop',)

def p_procedure_call(p):
    'pro' #Incompleto
