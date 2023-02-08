import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'VARS',
    'PROCS',
    'ROBOT',
    'COMMAND',
    'CONTROL',
    'CONDITION',
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'DO',
    'REPEAT',
    'FACING',
    'CANPUT',
    'CANPICK',
    'CANMOVEINDIR',
    'CANJUMPINDIR',
    'CANMOVETOTHE',
    'CANJUMPTOTHE',
    'NOT',
    'NORTH',
    'SOUTH',
    'EAST',
    'WEST',
    'FRONT',
    'RIGHT',
    'LEFT',
    'BACK',
    'BALLOONS',
    'CHIPS',
    'NOP',
    'ASSIGNTO',
    'GOTO',
    'MOVE',
    'TURN',
    'FACE',
    'PUT',
    'PICK',
    'MOVETOTHE',
    'MOVEINDIR',
    'JUMPTOTHE',
    'JUMPINDIR'
]

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in ['VARS', 'PROCS', 'ROBOT']:
        t.type = t.value.upper()
    elif t.value.upper() in ['ASSIGNTO', 'GOTO', 'MOVE', 'TURN', 'FACE', 'PUT', 'PICK', 'MOVETOTHE', 'MOVEINDIR', 'JUMPTOTHE', 'JUMPINDIR', 'NOP']:
        t.type = 'COMMAND'
    elif t.value.upper() in ['IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'REPEAT']:
        t.type = 'CONTROL'
    elif t.value.upper() in ['FACING', 'CANPUT', 'CANPICK', 'CANMOVE
