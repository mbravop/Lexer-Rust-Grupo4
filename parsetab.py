
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASSIGN ASYNC AWAIT BREAK COLON COMMA CONST CONTINUE CRATE DIFFERENTFROM DIVIDE DOT DOUBLEQUOTE DYN ELSE ENUM EQUALITY EXTERN FALSE FLOAT FN FOR GREATEREQUALSTHAN GREATERTHAN ID IF IMPL IN INTEGER IO LBRACKET LCURLYBRACKET LESSEQUALSTHAN LESSTHAN LET LOOP LPAREN MATCH MINUS MOD MODULE MOVE MULT MUT NOT OR PLUS PRINT PRINTLN PUB RBRACKET RCURLYBRACKET READLINE REF RETURN RPAREN SEMICOLON SINGLEQUOTE STATIC STD STDIN STRUCT SUPER Self TRAIT TRUE TYPE UNSAFE USE WHERE WHILE selffuncion : FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKETcodigo : expresionAritmetica \n              | impresion SEMICOLON\n              | condiciones \n              | asignacion\n              | estrFor\n              | estrWhile\n              | input SEMICOLON\n              | codigoexpresionAritmetica : valor operador valor\n                           | valor operador expresionAritmeticaoperador : PLUS\n                | MINUS\n                | MULT\n                | DIVIDE\n                | MODvalor : INTEGER\n             | FLOAT\n             | IDvalores : valor\n               | valor COMMA valoresimpresion : PRINTLN NOT LPAREN valores RPAREN\n                 | PRINTLN NOT LPAREN valor RPARENinput : STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPARENcondicion : valor operComp valoroperComp : GREATERTHAN\n                | LESSTHAN\n                | EQUALITY\n                | DIFFERENTFROM\n                | GREATEREQUALSTHAN\n                | LESSEQUALSTHANcondiciones : condicion\n                   | condicion conector condicionescondicion : TRUE\n                 | FALSEconector : AND\n                | ORasignacion : LET ID ASSIGN valor\n                    | LET ID ASSIGN condiciones\n                    | LET ID ASSIGN expresionAritmeticaasignacion : LET ID ASSIGN estructurasestructuras : tupla\n                    | arraytupla : LPAREN valores RPARENtupla : LPAREN RPARENarray : LBRACKET valores RBRACKETarray : LBRACKET RBRACKETestrWhile : WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKETestrFor : FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET'
    
_lr_action_items = {'FN':([0,],[2,]),'$end':([1,27,],[0,-1,]),'ID':([2,6,19,20,21,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,55,57,58,59,69,70,76,82,98,],[3,7,47,48,7,7,7,-12,-13,-14,-15,-16,-26,-27,-28,-29,-30,-31,7,-36,-37,7,7,71,7,7,7,7,7,99,]),'LPAREN':([3,43,57,91,95,],[4,55,69,92,96,]),'RPAREN':([4,7,23,24,61,62,69,77,79,85,92,99,],[5,-19,-17,-18,74,75,78,86,-20,-21,93,100,]),'LCURLYBRACKET':([5,7,18,23,24,25,26,49,54,56,71,],[6,-19,-32,-17,-18,-34,-35,59,-25,-33,82,]),'PRINTLN':([6,59,82,],[17,17,17,]),'LET':([6,59,82,],[19,19,19,]),'FOR':([6,59,82,],[20,20,20,]),'WHILE':([6,59,82,],[21,21,21,]),'STD':([6,59,82,],[22,22,22,]),'INTEGER':([6,21,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,55,57,59,69,70,76,82,],[23,23,23,23,-12,-13,-14,-15,-16,-26,-27,-28,-29,-30,-31,23,-36,-37,23,23,23,23,23,23,23,]),'FLOAT':([6,21,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,55,57,59,69,70,76,82,],[24,24,24,24,-12,-13,-14,-15,-16,-26,-27,-28,-29,-30,-31,24,-36,-37,24,24,24,24,24,24,24,]),'TRUE':([6,21,44,45,46,57,59,82,],[25,25,25,-36,-37,25,25,25,]),'FALSE':([6,21,44,45,46,57,59,82,],[26,26,26,-36,-37,26,26,26,]),'PLUS':([7,16,23,24,52,63,],[-19,32,-17,-18,32,32,]),'MINUS':([7,16,23,24,52,63,],[-19,33,-17,-18,33,33,]),'MULT':([7,16,23,24,52,63,],[-19,34,-17,-18,34,34,]),'DIVIDE':([7,16,23,24,52,63,],[-19,35,-17,-18,35,35,]),'MOD':([7,16,23,24,52,63,],[-19,36,-17,-18,36,36,]),'GREATERTHAN':([7,16,23,24,50,63,],[-19,37,-17,-18,37,37,]),'LESSTHAN':([7,16,23,24,50,63,],[-19,38,-17,-18,38,38,]),'EQUALITY':([7,16,23,24,50,63,],[-19,39,-17,-18,39,39,]),'DIFFERENTFROM':([7,16,23,24,50,63,],[-19,40,-17,-18,40,40,]),'GREATEREQUALSTHAN':([7,16,23,24,50,63,],[-19,41,-17,-18,41,41,]),'LESSEQUALSTHAN':([7,16,23,24,50,63,],[-19,42,-17,-18,42,42,]),'RCURLYBRACKET':([7,8,9,11,12,13,14,18,23,24,25,26,28,29,52,53,54,56,63,64,65,66,67,68,72,78,81,83,86,87,88,90,],[-19,27,-2,-4,-5,-6,-7,-32,-17,-18,-34,-35,-3,-8,-10,-11,-25,-33,-38,-39,-40,-41,-42,-43,83,-45,-47,-48,-44,-46,90,-49,]),'AND':([7,18,23,24,25,26,54,],[-19,45,-17,-18,-34,-35,-25,]),'OR':([7,18,23,24,25,26,54,],[-19,46,-17,-18,-34,-35,-25,]),'COMMA':([7,23,24,62,79,],[-19,-17,-18,76,76,]),'RBRACKET':([7,23,24,70,79,80,85,],[-19,-17,-18,81,-20,87,-21,]),'SEMICOLON':([10,15,74,75,100,],[28,29,-22,-23,-24,]),'NOT':([17,],[43,]),'COLON':([22,51,73,84,],[51,60,84,89,]),'ASSIGN':([47,],[57,]),'IN':([48,],[58,]),'LBRACKET':([57,],[70,]),'IO':([60,],[73,]),'STDIN':([89,],[91,]),'DOT':([93,],[94,]),'READLINE':([94,],[95,]),'REF':([96,],[97,]),'MUT':([97,],[98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'funcion':([0,],[1,]),'codigo':([6,59,82,],[8,72,88,]),'expresionAritmetica':([6,30,57,59,82,],[9,53,65,9,9,]),'impresion':([6,59,82,],[10,10,10,]),'condiciones':([6,21,44,57,59,82,],[11,49,56,64,11,11,]),'asignacion':([6,59,82,],[12,12,12,]),'estrFor':([6,59,82,],[13,13,13,]),'estrWhile':([6,59,82,],[14,14,14,]),'input':([6,59,82,],[15,15,15,]),'valor':([6,21,30,31,44,55,57,59,69,70,76,82,],[16,50,52,54,50,62,63,16,79,79,79,16,]),'condicion':([6,21,44,57,59,82,],[18,18,18,18,18,18,]),'operador':([16,52,63,],[30,30,30,]),'operComp':([16,50,63,],[31,31,31,]),'conector':([18,],[44,]),'valores':([55,69,70,76,],[61,77,80,85,]),'estructuras':([57,],[66,]),'tupla':([57,],[67,]),'array':([57,],[68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> funcion","S'",1,None,None,None),
  ('funcion -> FN ID LPAREN RPAREN LCURLYBRACKET codigo RCURLYBRACKET','funcion',7,'p_funcion','parser.py',7),
  ('codigo -> expresionAritmetica','codigo',1,'p_codigo','parser.py',11),
  ('codigo -> impresion SEMICOLON','codigo',2,'p_codigo','parser.py',12),
  ('codigo -> condiciones','codigo',1,'p_codigo','parser.py',13),
  ('codigo -> asignacion','codigo',1,'p_codigo','parser.py',14),
  ('codigo -> estrFor','codigo',1,'p_codigo','parser.py',15),
  ('codigo -> estrWhile','codigo',1,'p_codigo','parser.py',16),
  ('codigo -> input SEMICOLON','codigo',2,'p_codigo','parser.py',17),
  ('codigo -> codigo','codigo',1,'p_codigo','parser.py',18),
  ('expresionAritmetica -> valor operador valor','expresionAritmetica',3,'p_expresionAritmetica','parser.py',22),
  ('expresionAritmetica -> valor operador expresionAritmetica','expresionAritmetica',3,'p_expresionAritmetica','parser.py',23),
  ('operador -> PLUS','operador',1,'p_operador','parser.py',26),
  ('operador -> MINUS','operador',1,'p_operador','parser.py',27),
  ('operador -> MULT','operador',1,'p_operador','parser.py',28),
  ('operador -> DIVIDE','operador',1,'p_operador','parser.py',29),
  ('operador -> MOD','operador',1,'p_operador','parser.py',30),
  ('valor -> INTEGER','valor',1,'p_valor','parser.py',34),
  ('valor -> FLOAT','valor',1,'p_valor','parser.py',35),
  ('valor -> ID','valor',1,'p_valor','parser.py',36),
  ('valores -> valor','valores',1,'p_valores','parser.py',39),
  ('valores -> valor COMMA valores','valores',3,'p_valores','parser.py',40),
  ('impresion -> PRINTLN NOT LPAREN valores RPAREN','impresion',5,'p_impresion','parser.py',43),
  ('impresion -> PRINTLN NOT LPAREN valor RPAREN','impresion',5,'p_impresion','parser.py',44),
  ('input -> STD COLON COLON IO COLON COLON STDIN LPAREN RPAREN DOT READLINE LPAREN REF MUT ID RPAREN','input',16,'p_input','parser.py',49),
  ('condicion -> valor operComp valor','condicion',3,'p_condicion','parser.py',53),
  ('operComp -> GREATERTHAN','operComp',1,'p_operComp','parser.py',56),
  ('operComp -> LESSTHAN','operComp',1,'p_operComp','parser.py',57),
  ('operComp -> EQUALITY','operComp',1,'p_operComp','parser.py',58),
  ('operComp -> DIFFERENTFROM','operComp',1,'p_operComp','parser.py',59),
  ('operComp -> GREATEREQUALSTHAN','operComp',1,'p_operComp','parser.py',60),
  ('operComp -> LESSEQUALSTHAN','operComp',1,'p_operComp','parser.py',61),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','parser.py',64),
  ('condiciones -> condicion conector condiciones','condiciones',3,'p_condiciones','parser.py',65),
  ('condicion -> TRUE','condicion',1,'p_condicionBool','parser.py',68),
  ('condicion -> FALSE','condicion',1,'p_condicionBool','parser.py',69),
  ('conector -> AND','conector',1,'p_conector','parser.py',72),
  ('conector -> OR','conector',1,'p_conector','parser.py',73),
  ('asignacion -> LET ID ASSIGN valor','asignacion',4,'p_asignacion','parser.py',77),
  ('asignacion -> LET ID ASSIGN condiciones','asignacion',4,'p_asignacion','parser.py',78),
  ('asignacion -> LET ID ASSIGN expresionAritmetica','asignacion',4,'p_asignacion','parser.py',79),
  ('asignacion -> LET ID ASSIGN estructuras','asignacion',4,'p_asignacionEstructuras','parser.py',83),
  ('estructuras -> tupla','estructuras',1,'p_estructuras','parser.py',86),
  ('estructuras -> array','estructuras',1,'p_estructuras','parser.py',87),
  ('tupla -> LPAREN valores RPAREN','tupla',3,'p_tupla','parser.py',90),
  ('tupla -> LPAREN RPAREN','tupla',2,'p_tuplaVacia','parser.py',93),
  ('array -> LBRACKET valores RBRACKET','array',3,'p_array','parser.py',96),
  ('array -> LBRACKET RBRACKET','array',2,'p_arrayVacio','parser.py',99),
  ('estrWhile -> WHILE condiciones LCURLYBRACKET codigo RCURLYBRACKET','estrWhile',5,'p_estrWhile','parser.py',103),
  ('estrFor -> FOR ID IN ID LCURLYBRACKET codigo RCURLYBRACKET','estrFor',7,'p_estrFor','parser.py',106),
]
