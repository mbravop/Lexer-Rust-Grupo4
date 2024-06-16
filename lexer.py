import ply.lex as lex
from datetime import datetime
#Palabras reservadas - Mauricio Bravo
reserved = {'as':'AS','break':'BREAK','const':'CONST','continue':'CONTINUE','crate':'CRATE','else':'ELSE','enum':'ENUM','extern':'EXTERN','false':'FALSE','fn':'FN','for':'FOR','if':'IF','impl':'IMPL','in':'IN','let':'LET','loop':'LOOP','match':'MATCH','mod':'MOD','move':'MOVE','mut':'MUT','pub':'PUB','ref':'REF','return':'RETURN','self':'self','Self':'Self','static':'STATIC','struct':'STRUCT','super':'SUPER','trait':'TRAIT','true':'TRUE','type':'TYPE','unsafe':'UNSAFE','use':'USE','where':'WHERE','while':'WHILE','async':'ASYNC','await':'AWAIT','dyn':'DYN','print':'PRINT','println':'PRINTLN'}

#lista de los tokens - Dereck Santander
tokens = (
    'ID',
    'INTEGER',
    'FLOAT',
    'CHAR',
    'STRING',
    'PLUS',
    'MINUS',
    'MULT',
    'DIVIDE',
    'ASSIGN',
    'MODULE',
    'LPAREN',
    'RPAREN',
    'COLON',
    'GREATERTHAN',
    'LESSTHAN',
    'GREATEREQUALSTHAN', 
    'LESSEQUALSTHAN', 
    'EQUALITY', 
    'DIFFERENTFROM',
    'AND',
    'OR',
    'NOT',
    'LBRACKET',
    'RBRACKET',
    'LCURLYBRACKET',
    'RCURLYBRACKET',
    'SINGLEQUOTE',
    'DOUBLEQUOTE'
) + tuple(reserved.values())

#Expresiones regulares para tokens simples - Dereck
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'\/'
t_ASSIGN = r'='
t_MODULE = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_GREATERTHAN = r'>'
t_SINGLEQUOTE = r'\''
t_DOUBLEQUOTE = r'\"'
#Expresiones regulares para tokens simples - Mauricio
t_MULT = r'\*'
t_LESSTHAN = r'<'
t_GREATEREQUALSTHAN = r'>='
t_LESSEQUALSTHAN = r'<='
t_EQUALITY = r'=='
t_DIFFERENTFROM = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'

#Expresiones regulares para tokens complejos - Dereck Santander
def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'(-?\d+\.\d*)|(-?\d*\.\d+)'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'[\w\W]$'
    return t

def t_STRING(t):
    r'[\w\W]{2,}'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  if else print abc123print_ 14.5
  "hola" '&' {[}]/hola true
  TRUE falSE false .ADADA
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)


#Funcion para logs - Mauricio Bravo
def crearLog(usuarioGit, salidaLexer):
    now = datetime.now()
    archivo = open("logs/lexico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    archivo.write(salidaLexer)
    archivo.close()


