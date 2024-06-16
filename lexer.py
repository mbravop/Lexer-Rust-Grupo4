import ply.lex as lex
from datetime import datetime
#Palabras reservadas - Mauricio Bravo
reserved = {'as':'AS','break':'BREAK','const':'CONST','continue':'CONTINUE','crate':'CRATE','else':'ELSE','enum':'ENUM','extern':'EXTERN','false':'FALSE','fn':'FN','for':'FOR','if':'IF','impl':'IMPL','in':'IN','let':'LET','loop':'LOOP','match':'MATCH','mod':'MOD','move':'MOVE','mut':'MUT','pub':'PUB','ref':'REF','return':'RETURN','self':'self','Self':'Self','static':'STATIC','struct':'STRUCT','super':'SUPER','trait':'TRAIT','true':'TRUE','type':'TYPE','unsafe':'UNSAFE','use':'USE','where':'WHERE','while':'WHILE','async':'ASYNC','await':'AWAIT','dyn':'DYN'}

#lista de los tokens - Dereck Santander
tokens = (
    'ID',
    'INTEGER',
    'FLOAT',
    'CHAR',
    'STRING',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'EQUALS',
    'MOD',
    'LPAREN',
    'RPAREN',
    'GREATERTHAN',
    'LESSTHAN',
    'GREATEREQUALSTHAN', 
    'LESSEQUALSTHAN', 
    'EQUALITY', 
    'DIFFERENTFROM',
    'AND',
    'OR',
    'NOT',
) + tuple(reserved.values())

#Expresiones regulares para tokens simples - Dereck(8 tokens)
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'\/'
t_EQUALS = r'='
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_GREATERTHAN = r'>'

#Expresiones regulares para tokens complejos - Dereck Santander
def t_ID(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT(t):
    r'(-?\d+\.\d*)|(-?\d*\.\d+)'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r'^\'[\w\W]\'$'
    return t

def t_STRING(t):
    r'^\"[\w\W]{2,}\"$'
    return t


#Funcion para logs - Mauricio Bravo
def crearLog(usuarioGit, salidaLexer):
    now = datetime.now()
    archivo = open("logs/lexico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    archivo.write(salidaLexer)
    archivo.close()


