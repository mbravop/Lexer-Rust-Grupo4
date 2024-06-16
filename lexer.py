import ply.lex as lex
from datetime import datetime
#Palabras reservadas - Mauricio Bravo
reserved = {'as':'AS','break':'BREAK','const':'CONST','continue':'CONTINUE','crate':'CRATE','else':'ELSE','enum':'ENUM','extern':'EXTERN','false':'FALSE','fn':'FN','for':'FOR','if':'IF','impl':'IMPL','in':'IN','let':'LET','loop':'LOOP','match':'MATCH','mod':'MOD','move':'MOVE','mut':'MUT','pub':'PUB','ref':'REF','return':'RETURN','self':'self','Self':'Self','static':'STATIC','struct':'STRUCT','super':'SUPER','trait':'TRAIT','true':'TRUE','type':'TYPE','unsafe':'UNSAFE','use':'USE','where':'WHERE','while':'WHILE','async':'ASYNC','await':'AWAIT','dyn':'DYN'}


#Funcion para logs - Mauricio Bravo
def crearLog(usuarioGit, salidaLexer):
    now = datetime.now()
    archivo = open("logs/lexico-"+usuarioGit+"-"+now.strftime("%d%m%Y-%Hh%M")+".txt","w")
    archivo.write(salidaLexer)
    archivo.close()
