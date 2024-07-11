import ply.lex as lex
from datetime import datetime
#Palabras reservadas - Mauricio Bravo
reserved = {'as':'AS','break':'BREAK','const':'CONST','continue':'CONTINUE','crate':'CRATE','else':'ELSE','enum':'ENUM','extern':'EXTERN','false':'FALSE','fn':'FN','for':'FOR','if':'IF','impl':'IMPL','in':'IN','let':'LET','loop':'LOOP','match':'MATCH','mod':'MOD','move':'MOVE','mut':'MUT','pub':'PUB','ref':'REF','return':'RETURN','self':'self','Self':'Self','static':'STATIC','struct':'STRUCT','super':'SUPER','trait':'TRAIT','true':'TRUE','type':'TYPE','unsafe':'UNSAFE','use':'USE','where':'WHERE','while':'WHILE','async':'ASYNC','await':'AWAIT','dyn':'DYN','print':'PRINT','println':'PRINTLN','io':'IO','stdin':'STDIN','readline':'READLINE','std':'STD'}

#lista de los tokens - Dereck Santander
tokens = (
    'COMMA',
    'ID',
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'MULT',
    'DIVIDE',
    'ASSIGN',
    'MODULE',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COLON',
    'SEMICOLON',
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
    'DOUBLEQUOTE',
    'STRING'
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
t_DOT = r'\.'
#Expresiones regulares para tokens simples - Mauricio
t_COMMA = r','
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
t_SEMICOLON = r';'


#Expresiones regulares para tokens complejos - Dereck Santander
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'(\d+\.\d*)|(\d*\.\d+)'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


errors = []
# Error handling rule
def t_error(t):
    errorMessage = "Illegal character '%s'" % t.value[0]
    errors.append(errorMessage)
    t.lexer.skip(1)


lexer = lex.lex()
def ejecutarLexer(entradaLexer):
    salida = []
    lexer.input(entradaLexer)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        salida.append(str(tok))

    if errors:
        salida.append("\nErrores:\n"+"\n".join(errors))

    return "\n".join(salida)

