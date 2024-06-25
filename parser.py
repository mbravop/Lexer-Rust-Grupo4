import ply.yacc as yacc
from lexer import tokens

def p_codigo(p):
    '''codigo : expresionAritmetica
              | condiciones
              | estrWhile'''

#expresiones aritméticas con uno o más operadores - Mauricio Bravo
def p_expresionAritmetica(p):
    '''expresionAritmetica : valor operador valor
                           | valor operador expresionAritmetica'''

def p_operador(p): # - Mauricio Bravo
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD'''

#condiciones con uno o más conectores - Mauricio Bravo
def p_condicion(p):
    'condicion : valor operComp valor'

def p_operComp(p): # - Mauricio Bravo
    '''operComp : MORETHAN
                | LESSTHAN
                | EQUITY
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

def p_estructuras(p):# - Mauricio Bravo
    '''estructuras : tupla'''

def p_tupla(p):# - Mauricio Bravo
    '''tupla : LPAREN valores RPAREN'''

def p_tuplaVacia(p):# - Mauricio Bravo
    'tupla : LPAREN RPAREN'

#declarar estructuras de control
def p_estrWhile(p): # - Mauricio Bravo
    'estrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET'


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)