import ply.yacc as yacc
from lexer import tokens


# Reglas semánticas
# Mauricio Bravo
# 1. Revisar que nombres de funciones no se repitan
# 2. Permitir operaciones entre valores numéricos

# Dereck Santamder
# 1. Verificar que las variables hayan sido incializadas
# 2. Revisar que las condiciones sean un valor tipo boolean


salidaSintactico = ""
salidaSemantico = ""



# Agregar variables declaradas - Dereck Santander
variables = {}

# Agregar funciones declaradas - Mauricio Bravo
listaFunciones = set([])

# Error semántico para log - Mauricio Bravo
errorSemantico = ""

def agregarErrorSintactico(mensaje):
    global salidaSintactico
    if mensaje!="None":
        salidaSintactico+=mensaje+"\n"

def agregarErrorSemantico(mensaje):
    global salidaSemantico
    salidaSemantico+=mensaje+"\n"

# Funcion general - Dereck Santander
def p_funcion(p):
    '''funcion : FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKET'''
    if p[2] in listaFunciones:
        errorSemantico = f"Error semantico. La función {p[2]} ya existe"
        agregarErrorSemantico(errorSemantico)
    else:
        listaFunciones.add(p[2])
    # New
    p[0] = p[6]


def p_codigo(p):
    '''codigo : expresionAritmetica codigo
              | impresion masCodigo
              | condiciones masCodigo
              | asignacion masCodigo
              | estrFor
              | estrWhile
              | input masCodigo
              | funciones
              | aumentador masCodigo'''

    # New
    p[0] = p[1]


def p_funciones(p):
    '''funciones : funcion
                 | funcion funciones'''

    # New
    p[0] = p[1]


def p_masCodigo(p):
    '''masCodigo : SEMICOLON
                | SEMICOLON codigo'''



# expresiones aritméticas con uno o más operadores - Mauricio Bravo
def p_expresionAritmetica(p):
    '''expresionAritmetica : valor operador valor
                            | valor operador expresionAritmetica'''

    # New
    if len(p) == 4:
        try:
            if isinstance(p[1],str) and p[1] not in variables:
                if p[1].count(".") == 1:
                    p[1] = float(p[1])
        except:
            pass

        try:
            if isinstance(p[3],str) and p[3] not in variables:
                if p[3].count(".") == 1:
                    p[3] = float(p[1])
        except:
            pass

        if not isinstance(p[1], str) or p[1] in variables:
            if not isinstance(p[1], (int,float)):
                errorSemantico = "Error semantico. No se pueden operar valores de tipo no numérico"
                agregarErrorSemantico(errorSemantico)
                return
            else:
                pass
        else:
            errorSemantico = f"Error semantico. La variable {p[1]} no ha sido inicializada"
            agregarErrorSemantico(errorSemantico)
            return

        if not isinstance(p[3], str) or p[3] in variables:
            if not isinstance(p[3], (int,float)):
                errorSemantico = "Error semantico. No se pueden operar valores de tipo no numérico"
                agregarErrorSemantico(errorSemantico)
                return
            else:
                pass
        else:
            errorSemantico = f"Error semantico. La variable {p[3]} no ha sido inicializada"
            agregarErrorSemantico(errorSemantico)
            return
    else:
        p[0] = eval(f"{p[1]} {p[2]} {p[3]}")


def p_operador(p):  # - Mauricio Bravo
    '''operador : PLUS
                | MINUS
                | MULT
                | DIVIDE
                | MOD'''
    p[0] = p[1]


# IMPRESION CON CERO, UNO, O MAS ARGUMENTOS - Dereck Santander
def p_valor(p):
    '''valor : INTEGER
             | FLOAT
             | ID'''
    # New
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    elif isinstance(p[1], int):
        p[0] = int(p[1])
    elif isinstance(p[1], float):
        p[0] = float(p[1])
    else:
        p[0] = p[1]


def p_valores(p):  # - Dereck Santander
    '''valores : valor
               | valor COMMA valores'''
    # New
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + [p[3]]


def p_impresion(p):  # - Dereck Santander
    '''impresion : PRINTLN NOT LPAREN valores RPAREN
                | PRINTLN NOT LPAREN STRING RPAREN'''

    # New
    p[0] = p[4]


# SOLICITUD DE DATOS POR TECLADO - Dereck Santander
def p_input(p):
    '''input : STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPAREN'''

    # New
    if not isinstance(p[15], str) or p[15] not in variables:
        errorSemantico = f"Error semantico. La variable {p[15]} no ha sido inicializada"
        agregarErrorSemantico(errorSemantico)



# condiciones con uno o más conectores - Mauricio Bravo
def p_condicion(p):
    'condicion : valor operComp valor'
    # New
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[1]} no ha sido inicializada"
        agregarErrorSemantico(errorSemantico)

    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[3]} no ha sido inicializada"
        agregarErrorSemantico(errorSemantico)

    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>=':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] < p[3]




def p_operComp(p):  # - Mauricio Brav
    '''operComp : GREATERTHAN
                | LESSTHAN
                | EQUALITY
                | DIFFERENTFROM
                | GREATEREQUALSTHAN
                | LESSEQUALSTHAN'''
    p[0] = p[1]


def p_condiciones(p):  # - Mauricio Bravo
    '''condiciones : condicion
                   | condicion conector condiciones'''

    # New
    if not isinstance(p[1], bool):
        errorSemantico = f"Error semantico. El valor {p[1]} no es de tipo boolean"
        agregarErrorSemantico(errorSemantico)
    else:
        if len(p) == 2:
            p[0] = p[1]
        else:
            if p[2] == '&&':
                p[0] = p[1] and p[3]
            else:
                p[0] = p[1] or p[3]


def p_condicionBool(p):  # - Mauricio Bravo
    '''condicion : TRUE
                 | FALSE'''
    p[0] = p[1]


def p_conector(p):  # - Mauricio Bravo
    '''conector : AND
                | OR'''
    p[0] = p[1]


# definición de variables, todos los tipos, almacena resultados de expresiones/condicionales - Dereck Santander
def p_asignacion(p):
    '''asignacion : LET ID ASSIGN valor
                    | LET ID ASSIGN condiciones
                    | LET ID ASSIGN expresionAritmetica'''

    # New
    variables[p[2]] = p[4]


# declarar estructuras de datos - Dereck Santander
def p_asignacionEstructuras(p):
    'asignacion : LET ID ASSIGN estructuras'

    # New
    variables[p[2]] = p[4]


def p_estructuras(p):  # - Mauricio Bravo
    '''estructuras : tupla
                    | array'''


def p_tupla(p):  # - Mauricio Bravo
    '''tupla : LPAREN valores RPAREN'''

    # New
    p[0] = tuple(p[2])


def p_tuplaVacia(p):  # - Mauricio Bravo
    'tupla : LPAREN RPAREN'

    p[0] = tuple(p[2])


def p_array(p):  # - Dereck Santander
    'array : LBRACKET valores RBRACKET'

    # New
    p[0] = list(p[2])


def p_arrayVacio(p):  # - Dereck Santander
    'array : LBRACKET RBRACKET'

    p[0] = list(p[2])


# declarar estructuras de control
def p_estrWhile(p):  # - Mauricio Bravo
    '''estrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET
                 | WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET codigo '''

    # New
    if not isinstance(p[2], bool):
        errorSemantico = f"Error semantico. El valor {p[2]} no es de tipo boolean"
        agregarErrorSemantico(errorSemantico)
    else:
        pass
    p[0] = p[4]

def p_aumentador(p):
    '''aumentador : ID PLUS ASSIGN valor
                  | ID MINUS ASSIGN valor'''

def p_estrFor(p):  # - Dereck Santander
    '''estrFor : FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET
                | FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET codigo'''

    # New
    if not isinstance(p[4], str) or p[4] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[4]} no ha sido inicializada"
        agregarErrorSemantico(errorSemantico)
    p[0] = p[6]


# Error rule for syntax errors
def p_error(p):
    mensaje = f"Error sintáctico: {p.value!r}'"
    agregarErrorSintactico(mensaje)


def p_impresion_error(p):
    'impresion : PRINTLN error'
    agregarErrorSintactico("Syntax error in print statement. Bad expression")


def p_expresionAritmetica_error(p):
    'expresionAritmetica : valor operador error'
    agregarErrorSintactico("Syntax error in expresionAritmetica statement. Bad expression")


def p_input_error(p):
    'input : STD error'
    agregarErrorSintactico("Syntax error in input statement. Bad expression")


def p_asignacion_error(p):
    'asignacion : LET error'
    agregarErrorSintactico("Syntax error in asignacion statement. Bad expression")


# Build the parser
parser = yacc.yacc()


def analizadorSintactico(codigo):
    result = parser.parse(codigo)
    global salidaSintactico
    salidaSintactico += str(result)
    return [salidaSintactico, salidaSemantico]
