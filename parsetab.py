
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASSIGN ASYNC AWAIT BREAK COLON COMMA CONST CONTINUE CRATE DIFFERENTFROM DIVIDE DOT DOUBLEQUOTE DYN ELSE ENUM EQUALITY EXTERN FALSE FLOAT FN FOR GREATEREQUALSTHAN GREATERTHAN ID IF IMPL IN INTEGER IO LBRACKET LCURLYBRACKET LESSEQUALSTHAN LESSTHAN LET LOOP LPAREN MATCH MINUS MOD MODULE MOVE MULT MUT NOT OR PLUS PRINT PRINTLN PUB RBRACKET RCURLYBRACKET READLINE REF RETURN RPAREN SEMICOLON SINGLEQUOTE STATIC STD STDIN STRING STRUCT SUPER Self TRAIT TRUE TYPE UNSAFE USE WHERE WHILE selffuncion : FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKETcodigo : expresionAritmetica codigo\n              | impresion masCodigo\n              | condiciones masCodigo\n              | asignacion masCodigo\n              | estrFor\n              | estrWhile\n              | input masCodigo\n              | funciones\n              | aumentador masCodigofunciones : funcion\n                 | funcion funcionesmasCodigo : SEMICOLON\n                | SEMICOLON codigoexpresionAritmetica : valor operador valor\n                            | valor operador expresionAritmeticaoperador : PLUS\n                | MINUS\n                | MULT\n                | DIVIDE\n                | MODvalor : INTEGER\n             | FLOAT\n             | IDvalores : valor\n               | valor COMMA valoresimpresion : PRINTLN NOT LPAREN valores RPAREN\n                | PRINTLN NOT LPAREN STRING RPARENinput : STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPARENcondicion : valor operComp valoroperComp : GREATERTHAN\n                | LESSTHAN\n                | EQUALITY\n                | DIFFERENTFROM\n                | GREATEREQUALSTHAN\n                | LESSEQUALSTHANcondiciones : condicion\n                   | condicion conector condicionescondicion : TRUE\n                 | FALSEconector : AND\n                | ORasignacion : LET ID ASSIGN valor\n                    | LET ID ASSIGN condiciones\n                    | LET ID ASSIGN expresionAritmeticaasignacion : LET ID ASSIGN estructurasestructuras : tupla\n                    | arraytupla : LPAREN valores RPARENtupla : LPAREN RPARENarray : LBRACKET valores RBRACKETarray : LBRACKET RBRACKETestrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET\n                 | WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET codigo aumentador : ID PLUS ASSIGN valor\n                  | ID MINUS ASSIGN valorestrFor : FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET\n                | FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET codigoimpresion : PRINTLN errorexpresionAritmetica : valor operador errorinput : STD errorasignacion : LET error'
    
_lr_action_items = {'FN':([0,6,9,25,26,27,32,35,63,70,71,72,78,103,104,112,],[2,2,2,2,-22,-23,-1,2,-24,-15,-16,-60,2,2,2,2,]),'$end':([1,32,],[0,-1,]),'ID':([2,6,9,21,22,23,26,27,35,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,63,67,68,70,71,72,74,76,77,78,91,92,98,103,104,112,121,],[3,7,7,58,60,63,-22,-23,7,63,63,-17,-18,-19,-20,-21,-31,-32,-33,-34,-35,-36,63,-41,-42,-24,63,63,-15,-16,-60,63,63,93,7,63,63,63,7,7,7,122,]),'LPAREN':([3,53,76,113,118,],[4,74,91,115,119,]),'RPAREN':([4,26,27,63,82,83,84,91,99,106,115,122,],[5,-22,-23,-24,96,97,-25,100,107,-26,116,123,]),'LCURLYBRACKET':([5,20,26,27,28,29,61,63,73,75,93,],[6,-37,-22,-23,-39,-40,78,-24,-30,-38,103,]),'PRINTLN':([6,9,26,27,35,63,70,71,72,78,103,104,112,],[19,19,-22,-23,19,-24,-15,-16,-60,19,19,19,19,]),'LET':([6,9,26,27,35,63,70,71,72,78,103,104,112,],[21,21,-22,-23,21,-24,-15,-16,-60,21,21,21,21,]),'FOR':([6,9,26,27,35,63,70,71,72,78,103,104,112,],[22,22,-22,-23,22,-24,-15,-16,-60,22,22,22,22,]),'WHILE':([6,9,26,27,35,63,70,71,72,78,103,104,112,],[23,23,-22,-23,23,-24,-15,-16,-60,23,23,23,23,]),'STD':([6,9,26,27,35,63,70,71,72,78,103,104,112,],[24,24,-22,-23,24,-24,-15,-16,-60,24,24,24,24,]),'INTEGER':([6,9,23,26,27,35,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,63,67,68,70,71,72,74,76,78,91,92,98,103,104,112,],[26,26,26,-22,-23,26,26,26,-17,-18,-19,-20,-21,-31,-32,-33,-34,-35,-36,26,-41,-42,-24,26,26,-15,-16,-60,26,26,26,26,26,26,26,26,26,]),'FLOAT':([6,9,23,26,27,35,40,41,42,43,44,45,46,47,48,49,50,51,52,55,56,57,63,67,68,70,71,72,74,76,78,91,92,98,103,104,112,],[27,27,27,-22,-23,27,27,27,-17,-18,-19,-20,-21,-31,-32,-33,-34,-35,-36,27,-41,-42,-24,27,27,-15,-16,-60,27,27,27,27,27,27,27,27,27,]),'TRUE':([6,9,23,26,27,35,55,56,57,63,70,71,72,76,78,103,104,112,],[28,28,28,-22,-23,28,28,-41,-42,-24,-15,-16,-60,28,28,28,28,28,]),'FALSE':([6,9,23,26,27,35,55,56,57,63,70,71,72,76,78,103,104,112,],[29,29,29,-22,-23,29,29,-41,-42,-24,-15,-16,-60,29,29,29,29,29,]),'PLUS':([7,18,26,27,63,70,85,],[30,42,-22,-23,-24,42,42,]),'MINUS':([7,18,26,27,63,70,85,],[31,43,-22,-23,-24,43,43,]),'MULT':([7,18,26,27,63,70,85,],[-24,44,-22,-23,-24,44,44,]),'DIVIDE':([7,18,26,27,63,70,85,],[-24,45,-22,-23,-24,45,45,]),'MOD':([7,18,26,27,63,70,85,],[-24,46,-22,-23,-24,46,46,]),'GREATERTHAN':([7,18,26,27,62,63,85,],[-24,47,-22,-23,47,-24,47,]),'LESSTHAN':([7,18,26,27,62,63,85,],[-24,48,-22,-23,48,-24,48,]),'EQUALITY':([7,18,26,27,62,63,85,],[-24,49,-22,-23,49,-24,49,]),'DIFFERENTFROM':([7,18,26,27,62,63,85,],[-24,50,-22,-23,50,-24,50,]),'GREATEREQUALSTHAN':([7,18,26,27,62,63,85,],[-24,51,-22,-23,51,-24,51,]),'LESSEQUALSTHAN':([7,18,26,27,62,63,85,],[-24,52,-22,-23,52,-24,52,]),'RCURLYBRACKET':([8,13,14,16,25,32,33,34,35,36,37,38,39,66,69,94,104,109,110,112,114,],[32,-6,-7,-9,-11,-1,-2,-3,-13,-4,-5,-8,-10,-12,-14,104,-53,112,-54,-57,-58,]),'SEMICOLON':([10,11,12,15,17,20,26,27,28,29,54,59,63,65,70,71,72,73,75,80,81,85,86,87,88,89,90,96,97,100,102,107,108,123,],[35,35,35,35,35,-37,-22,-23,-39,-40,-59,-62,-24,-61,-15,-16,-60,-30,-38,-55,-56,-43,-44,-45,-46,-47,-48,-27,-28,-50,-52,-49,-51,-29,]),'NOT':([19,],[53,]),'error':([19,21,24,40,42,43,44,45,46,],[54,59,65,72,-17,-18,-19,-20,-21,]),'AND':([20,26,27,28,29,63,73,],[56,-22,-23,-39,-40,-24,-30,]),'OR':([20,26,27,28,29,63,73,],[57,-22,-23,-39,-40,-24,-30,]),'COLON':([24,64,95,105,],[64,79,105,111,]),'COMMA':([26,27,63,84,],[-22,-23,-24,98,]),'RBRACKET':([26,27,63,84,92,101,106,],[-22,-23,-24,-25,102,108,-26,]),'ASSIGN':([30,31,58,],[67,68,76,]),'IN':([60,],[77,]),'STRING':([74,],[83,]),'LBRACKET':([76,],[92,]),'IO':([79,],[95,]),'STDIN':([111,],[113,]),'DOT':([116,],[117,]),'READLINE':([117,],[118,]),'REF':([119,],[120,]),'MUT':([120,],[121,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funcion':([0,6,9,25,35,78,103,104,112,],[1,25,25,25,25,25,25,25,25,]),'codigo':([6,9,35,78,103,104,112,],[8,33,69,94,109,110,114,]),'expresionAritmetica':([6,9,35,40,76,78,103,104,112,],[9,9,9,71,87,9,9,9,9,]),'impresion':([6,9,35,78,103,104,112,],[10,10,10,10,10,10,10,]),'condiciones':([6,9,23,35,55,76,78,103,104,112,],[11,11,61,11,75,86,11,11,11,11,]),'asignacion':([6,9,35,78,103,104,112,],[12,12,12,12,12,12,12,]),'estrFor':([6,9,35,78,103,104,112,],[13,13,13,13,13,13,13,]),'estrWhile':([6,9,35,78,103,104,112,],[14,14,14,14,14,14,14,]),'input':([6,9,35,78,103,104,112,],[15,15,15,15,15,15,15,]),'funciones':([6,9,25,35,78,103,104,112,],[16,16,66,16,16,16,16,16,]),'aumentador':([6,9,35,78,103,104,112,],[17,17,17,17,17,17,17,]),'valor':([6,9,23,35,40,41,55,67,68,74,76,78,91,92,98,103,104,112,],[18,18,62,18,70,73,62,80,81,84,85,18,84,84,84,18,18,18,]),'condicion':([6,9,23,35,55,76,78,103,104,112,],[20,20,20,20,20,20,20,20,20,20,]),'masCodigo':([10,11,12,15,17,],[34,36,37,38,39,]),'operador':([18,70,85,],[40,40,40,]),'operComp':([18,62,85,],[41,41,41,]),'conector':([20,],[55,]),'valores':([74,91,92,98,],[82,99,101,106,]),'estructuras':([76,],[88,]),'tupla':([76,],[89,]),'array':([76,],[90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> funcion","S'",1,None,None,None),
  ('funcion -> FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKET','funcion',7,'p_funcion','parser.py',40),
  ('codigo -> expresionAritmetica codigo','codigo',2,'p_codigo','parser.py',51),
  ('codigo -> impresion masCodigo','codigo',2,'p_codigo','parser.py',52),
  ('codigo -> condiciones masCodigo','codigo',2,'p_codigo','parser.py',53),
  ('codigo -> asignacion masCodigo','codigo',2,'p_codigo','parser.py',54),
  ('codigo -> estrFor','codigo',1,'p_codigo','parser.py',55),
  ('codigo -> estrWhile','codigo',1,'p_codigo','parser.py',56),
  ('codigo -> input masCodigo','codigo',2,'p_codigo','parser.py',57),
  ('codigo -> funciones','codigo',1,'p_codigo','parser.py',58),
  ('codigo -> aumentador masCodigo','codigo',2,'p_codigo','parser.py',59),
  ('funciones -> funcion','funciones',1,'p_funciones','parser.py',66),
  ('funciones -> funcion funciones','funciones',2,'p_funciones','parser.py',67),
  ('masCodigo -> SEMICOLON','masCodigo',1,'p_masCodigo','parser.py',74),
  ('masCodigo -> SEMICOLON codigo','masCodigo',2,'p_masCodigo','parser.py',75),
  ('expresionAritmetica -> valor operador valor','expresionAritmetica',3,'p_expresionAritmetica','parser.py',81),
  ('expresionAritmetica -> valor operador expresionAritmetica','expresionAritmetica',3,'p_expresionAritmetica','parser.py',82),
  ('operador -> PLUS','operador',1,'p_operador','parser.py',128),
  ('operador -> MINUS','operador',1,'p_operador','parser.py',129),
  ('operador -> MULT','operador',1,'p_operador','parser.py',130),
  ('operador -> DIVIDE','operador',1,'p_operador','parser.py',131),
  ('operador -> MOD','operador',1,'p_operador','parser.py',132),
  ('valor -> INTEGER','valor',1,'p_valor','parser.py',138),
  ('valor -> FLOAT','valor',1,'p_valor','parser.py',139),
  ('valor -> ID','valor',1,'p_valor','parser.py',140),
  ('valores -> valor','valores',1,'p_valores','parser.py',153),
  ('valores -> valor COMMA valores','valores',3,'p_valores','parser.py',154),
  ('impresion -> PRINTLN NOT LPAREN valores RPAREN','impresion',5,'p_impresion','parser.py',163),
  ('impresion -> PRINTLN NOT LPAREN STRING RPAREN','impresion',5,'p_impresion','parser.py',164),
  ('input -> STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPAREN','input',16,'p_input','parser.py',172),
  ('condicion -> valor operComp valor','condicion',3,'p_condicion','parser.py',183),
  ('operComp -> GREATERTHAN','operComp',1,'p_operComp','parser.py',214),
  ('operComp -> LESSTHAN','operComp',1,'p_operComp','parser.py',215),
  ('operComp -> EQUALITY','operComp',1,'p_operComp','parser.py',216),
  ('operComp -> DIFFERENTFROM','operComp',1,'p_operComp','parser.py',217),
  ('operComp -> GREATEREQUALSTHAN','operComp',1,'p_operComp','parser.py',218),
  ('operComp -> LESSEQUALSTHAN','operComp',1,'p_operComp','parser.py',219),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','parser.py',224),
  ('condiciones -> condicion conector condiciones','condiciones',3,'p_condiciones','parser.py',225),
  ('condicion -> TRUE','condicion',1,'p_condicionBool','parser.py',242),
  ('condicion -> FALSE','condicion',1,'p_condicionBool','parser.py',243),
  ('conector -> AND','conector',1,'p_conector','parser.py',248),
  ('conector -> OR','conector',1,'p_conector','parser.py',249),
  ('asignacion -> LET ID ASSIGN valor','asignacion',4,'p_asignacion','parser.py',255),
  ('asignacion -> LET ID ASSIGN condiciones','asignacion',4,'p_asignacion','parser.py',256),
  ('asignacion -> LET ID ASSIGN expresionAritmetica','asignacion',4,'p_asignacion','parser.py',257),
  ('asignacion -> LET ID ASSIGN estructuras','asignacion',4,'p_asignacionEstructuras','parser.py',265),
  ('estructuras -> tupla','estructuras',1,'p_estructuras','parser.py',272),
  ('estructuras -> array','estructuras',1,'p_estructuras','parser.py',273),
  ('tupla -> LPAREN valores RPAREN','tupla',3,'p_tupla','parser.py',277),
  ('tupla -> LPAREN RPAREN','tupla',2,'p_tuplaVacia','parser.py',284),
  ('array -> LBRACKET valores RBRACKET','array',3,'p_array','parser.py',290),
  ('array -> LBRACKET RBRACKET','array',2,'p_arrayVacio','parser.py',297),
  ('estrWhile -> WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET','estrWhile',5,'p_estrWhile','parser.py',304),
  ('estrWhile -> WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET codigo','estrWhile',6,'p_estrWhile','parser.py',305),
  ('aumentador -> ID PLUS ASSIGN valor','aumentador',4,'p_aumentador','parser.py',316),
  ('aumentador -> ID MINUS ASSIGN valor','aumentador',4,'p_aumentador','parser.py',317),
  ('estrFor -> FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET','estrFor',7,'p_estrFor','parser.py',320),
  ('estrFor -> FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET codigo','estrFor',8,'p_estrFor','parser.py',321),
  ('impresion -> PRINTLN error','impresion',2,'p_impresion_error','parser.py',339),
  ('expresionAritmetica -> valor operador error','expresionAritmetica',3,'p_expresionAritmetica_error','parser.py',344),
  ('input -> STD error','input',2,'p_input_error','parser.py',349),
  ('asignacion -> LET error','asignacion',2,'p_asignacion_error','parser.py',354),
]
