import ply.yacc as yacc
from lexer import tokens
from datetime import datetime

#Funcion general - Dereck Santander
def p_funcion(p):
    '''funcion : FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKET'''


def p_codigo(p):
    '''codigo : expresionAritmetica masCodigo
              | impresion masCodigo
              | condiciones 
              | asignacion masCodigo
              | estrFor
              | estrWhile
              | input masCodigo'''

def p_masCodigo(p):
    '''masCodigo : SEMICOLON
                | SEMICOLON codigo'''

#expresiones aritméticas con uno o más operadores - Mauricio Bravo
def p_expresionAritmetica(p):
    '''expresionAritmetica : valor operador valor
                           | valor operador expresionAritmetica'''

def p_operador(p): # - Mauricio Bravo
    '''operador : PLUS
                | MINUS
                | MULT
                | DIVIDE
                | MOD'''
    
#IMPRESION CON CERO, UNO, O MAS ARGUMENTOS - Dereck Santander
def p_valor(p):
    '''valor : INTEGER
             | FLOAT
             | ID'''

def p_valores(p): # - Dereck Santander
    '''valores : valor
               | valor COMMA valores'''

def p_impresion(p): # - Dereck Santander
    'impresion : PRINTLN NOT LPAREN valores RPAREN'


#SOLICITUD DE DATOS POR TECLADO - Dereck Santander
def p_input(p):
    '''input : STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPAREN'''

#condiciones con uno o más conectores - Mauricio Bravo
def p_condicion(p):
    'condicion : valor operComp valor'

def p_operComp(p): # - Mauricio Bravo
    '''operComp : GREATERTHAN
                | LESSTHAN
                | EQUALITY
                | DIFFERENTFROM
                | GREATEREQUALSTHAN
                | LESSEQUALSTHAN'''

def p_condiciones(p): # - Mauricio Bravo
    '''condiciones : condicion
                   | condicion conector condiciones'''

def p_condicionBool(p):# - Mauricio Bravo
    '''condicion : TRUE
                 | FALSE'''

def p_conector(p): # - Mauricio Bravo
    '''conector : AND
                | OR'''

#definición de variables, todos los tipos, almacena resultados de expresiones/condicionales - Dereck Santander
def p_asignacion(p):
    '''asignacion : LET ID ASSIGN valor
                    | LET ID ASSIGN condiciones
                    | LET ID ASSIGN expresionAritmetica'''
    
#declarar estructuras de datos - Dereck Santander
def p_asignacionEstructuras(p):
    'asignacion : LET ID ASSIGN estructuras'

def p_estructuras(p):# - Mauricio Bravo
    '''estructuras : tupla
                    | array'''

def p_tupla(p):# - Mauricio Bravo
    '''tupla : LPAREN valores RPAREN'''

def p_tuplaVacia(p):# - Mauricio Bravo
    'tupla : LPAREN RPAREN'

def p_array(p): # - Dereck Santander
    'array : LBRACKET valores RBRACKET'

def p_arrayVacio(p): # - Dereck Santander
    'array : LBRACKET RBRACKET'

#declarar estructuras de control
def p_estrWhile(p): # - Mauricio Bravo
    '''estrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET
                 | WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET codigo '''

def p_estrFor(p): # - Dereck Santander
    '''estrFor : FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET
                | FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET codigo'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()



def crearLogParser(usuarioGit):
    now = datetime.now()
    archivo = open("logs/sintactico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    s=""
    while s!="SALIR":
        try:
            s = input('lp > ')
            if s != "SALIR":
                archivo.write("lp > "+s+"\n")
        except EOFError:
            archivo.write("Syntax error in input!")
            break
        if not s: continue
        result = parser.parse(s)
        print(result) # type: ignore
        if s!="SALIR":
            archivo.write(str(result)+"\n")
    archivo.close()

crearLogParser("mbravop")
#crearLogParser("DereckSantander")
