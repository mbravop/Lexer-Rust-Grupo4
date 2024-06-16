import ply.lex as lex
from datetime import datetime
#Palabras reservadas - Mauricio Bravo
reserved = {'as':'AS','break':'BREAK','const':'CONST','continue':'CONTINUE','crate':'CRATE','else':'ELSE','enum':'ENUM','extern':'EXTERN','false':'FALSE','fn':'FN','for':'FOR','if':'IF','impl':'IMPL','in':'IN','let':'LET','loop':'LOOP','match':'MATCH','mod':'MOD','move':'MOVE','mut':'MUT','pub':'PUB','ref':'REF','return':'RETURN','self':'self','Self':'Self','static':'STATIC','struct':'STRUCT','super':'SUPER','trait':'TRAIT','true':'TRUE','type':'TYPE','unsafe':'UNSAFE','use':'USE','where':'WHERE','while':'WHILE','async':'ASYNC','await':'AWAIT','dyn':'DYN','print':'PRINT','println':'PRINTLN'}

#lista de los tokens - Dereck Santander
tokens = (
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
t_SEMICOLON = r';'

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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Test it out
algoritmo = '''fn main() {
let num1 = 4;
let num2 = 6;
res = num1 + num2;
if (res > 10){
println!("Mayor que 10");
}else{
println!("No mayor");
}
'''

algoritmo2 = '''
    fn main() {
        let mut contador = 1;

        while contador <= 5 {
            println!("El contador es: {}", contador);
            contador += 1;
        }

        for numero in 1..=5 {
            println!("El numero es: {}", numero);
        }
    }
'''

def ejecutarLexer(entradaLexer):
    salida = []
    lexer = lex.lex()
    lexer.input(algoritmo)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        salida.append(str(tok))
    return "\n".join(salida)

#Funcion para logs - Mauricio Bravo
def crearLog(usuarioGit, entradaLexer):
    now = datetime.now()
    archivo = open("logs/lexico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    archivo.write(entradaLexer+"\n")
    archivo.write(ejecutarLexer(entradaLexer))
    archivo.close()

crearLog("mbravop",algoritmo)
crearLog("DereckSantander",algoritmo2)