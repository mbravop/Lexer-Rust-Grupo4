import ply.yacc as yacc
from lexer import tokens
from datetime import datetime

def crearLogSemantico(usuarioGit):
    now = datetime.now()
    archivoSemantico = open("logs/semantico-" + usuarioGit + "-" + now.strftime("%d%m%Y-%Hh%M") + ".txt", "w")
    return archivoSemantico


def cerrarLogSemantico(archivo):
    archivo.close()

archivoSemantico = crearLogSemantico("DereckSantander")

#Agregar variables declaradas - Dereck Santander
variables = {}

#Agregar funciones declaradas - Mauricio Bravo
listaFunciones = set([])

#Error semántico para log - Mauricio Bravo
errorSemanticoDefault = "No hay errores semánticos."
errorSemantico = errorSemanticoDefault

#Funcion general - Dereck Santander
def p_funcion(p):
    '''funcion : FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKET'''
    if p[2] in listaFunciones:
        errorSemantico = f"Error semantico. La función {p[2]} ya existe"
        print(errorSemantico)
        archivoSemantico.write(errorSemantico + "\n")
        errorSemantico = errorSemanticoDefault
    else:
        listaFunciones.add(p[2])
    #New
    p[0] = p[6]

def p_codigo(p):
    '''codigo : expresionAritmetica masCodigo
              | impresion masCodigo
              | condiciones masCodigo
              | asignacion masCodigo
              | estrFor
              | estrWhile
              | input masCodigo
              | funciones'''

    #New
    p[0] = p[1]

def p_funciones(p):
    '''funciones : funcion
                 | funcion funciones'''
    
    #New
    p[0] = p[1]

def p_masCodigo(p):
    '''masCodigo : SEMICOLON
                | SEMICOLON codigo'''

#expresiones aritméticas con uno o más operadores - Mauricio Bravo
def p_expresionAritmetica(p):
    '''expresionAritmetica : valor operador valor
                           | valor operador expresionAritmetica'''
    
    #New
    if len(p) == 4:
        if not isinstance(p[1],str) or p[1] in variables:
            if not isinstance(p[1],int):
                errorSemantico = "Error semantico. No se pueden operar valores de tipo no numérico"
                print(errorSemantico)
                archivoSemantico.write(errorSemantico + "\n")
                errorSemantico = errorSemanticoDefault
                return
            else:
                pass
        else:
            errorSemantico = f"Error semantico. La variable {p[1]} no ha sido inicializada"
            print(errorSemantico)
            archivoSemantico.write(errorSemantico + "\n")
            errorSemantico = errorSemanticoDefault
            return

        if not isinstance(p[3],str) or p[3] in variables:
            if not isinstance(p[3],int):
                errorSemantico = "Error semantico. No se pueden operar valores de tipo no numérico"
                print(errorSemantico)
                archivoSemantico.write(errorSemantico + "\n")
                errorSemantico = errorSemanticoDefault
                return
            else:
                pass
        else:
            errorSemantico = f"Error semantico. La variable {p[3]} no ha sido inicializada"
            print(errorSemantico)
            archivoSemantico.write(errorSemantico + "\n")
            errorSemantico = errorSemanticoDefault
            return
    else:
        p[0] = [p[1]] + p[3]

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
    #New
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    elif isinstance(p[1],int):
        p[0]= int(p[1])
    elif isinstance(p[1],float):
        p[0] = float(p[1])
    else:
        p[0] = p[1]

def p_valores(p): # - Dereck Santander
    '''valores : valor
               | valor COMMA valores'''
    #New
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_impresion(p): # - Dereck Santander
    'impresion : PRINTLN NOT LPAREN valores RPAREN'

    #New
    p[0] = p[4]

#SOLICITUD DE DATOS POR TECLADO - Dereck Santander
def p_input(p):
    '''input : STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPAREN'''

    #New
    if not isinstance(p[15],str) or p[15] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[15]} no ha sido inicializada"
        print(errorSemantico)
        archivoSemantico.write(errorSemantico + "\n")
        errorSemantico = errorSemanticoDefault

#condiciones con uno o más conectores - Mauricio Bravo
def p_condicion(p):
    'condicion : valor operComp valor'

    #New
    if not isinstance(p[1],str) or p[1] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[1]} no ha sido inicializada"
        print(errorSemantico)
        archivoSemantico.write(errorSemantico + "\n")
        errorSemantico = errorSemanticoDefault

    if not isinstance(p[3],str) or p[3] in variables:
        pass
    else:
        errorSemantico = f"Error semantico. La variable {p[3]} no ha sido inicializada"
        print(errorSemantico)
        archivoSemantico.write(errorSemantico + "\n")
        errorSemantico = errorSemanticoDefault


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
    
    #New
    if len(p) == 2:
            p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

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
    
    #New
    variables[p[2]] = p[4] 
    
#declarar estructuras de datos - Dereck Santander
def p_asignacionEstructuras(p):
    'asignacion : LET ID ASSIGN estructuras'
    
    #New
    variables[p[2]] = p[4] 

def p_estructuras(p):# - Mauricio Bravo
    '''estructuras : tupla
                    | array'''
    

def p_tupla(p):# - Mauricio Bravo
    '''tupla : LPAREN valores RPAREN'''

    #New
    p[0] = tuple(p[2])

def p_tuplaVacia(p):# - Mauricio Bravo
    'tupla : LPAREN RPAREN'

def p_array(p): # - Dereck Santander
    'array : LBRACKET valores RBRACKET'

    #New
    p[0] = list(p[2])

def p_arrayVacio(p): # - Dereck Santander
    'array : LBRACKET RBRACKET'

#declarar estructuras de control
def p_estrWhile(p): # - Mauricio Bravo
    '''estrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET
                 | WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET codigo '''
    
    #New
    p[0] = p[4]

def p_estrFor(p): # - Dereck Santander
    '''estrFor : FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET
                | FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET codigo'''
    
    #New
    p[0] = p[4]
    

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()



def crearLogParser(usuarioGit, archivoSem):
    now = datetime.now()
    archivoSintactico = open("logs/sintactico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    s=""
    while s!="SALIR":
        try:
            s = input('lp > ')
            if s != "SALIR":
                archivoSintactico.write("lp > "+s+"\n")
                archivoSem.write("lp > "+s+"\n")
        except EOFError:
            archivoSintactico.write("Syntax error in input!")
            break
        if not s: continue
        result = parser.parse(s)
        print(result) # type: ignore
        if s!="SALIR":
            archivoSintactico.write(str(result)+"\n")
    archivoSintactico.close()




crearLogParser("DereckSantander", archivoSemantico)
#crearLogParser("DereckSantander")
cerrarLogSemantico(archivoSemantico)
