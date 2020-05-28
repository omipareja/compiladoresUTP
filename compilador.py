import sys
import ply.lex as lex

#Juan Camilo Blanco Martinez 1088352177
#Aldahir Rojas Lancheros  1225089405
#Juan Manuel Sánchez Pareja 1010107723

#Lista de tokens


tokens = (
		#simbolos
		'PARENIZQUIERDA', 'PARENDERECHA','DOLAR','PUNTOYCOMA','PUNTO','COMA','DOSPUNTOS','LLAVEIZQ','LLAVEDER',
		'CORCHIZQ','CORCHDER','AMPERSAND','PLUS','PLUSPLUS','MINUS','MINUSMINUS','DIVIDE','MULTI','MENORQ','MAYORQ',
		'IGUAL','DIFERENTE','IQUALIQUAL','COMILLA',


		# palabras reservadas
		'IF','ELSE','DO','WHILE','FOR','SWITCH','CASE','LOGAND','LOGOR','LOGY','LOGXOR','LOGNEGACION',
		'BREAK','CONTINUE','DEFAULT',
		'INICIO','FIN','STATIC','CONST','PRINT','FUNCTION','RETURN','NULL','CLASS','PUBLIC','PRIVATE','NEW','EXTENDS',

		#otros
		'NUMERO','IDENTIFICADOR'
		#,'TAB','ESP','SALTO'

		)


#Reglas de expresiones regulares para tokens simples
t_COMILLA =r'\"'
t_PARENIZQUIERDA =r'\('
t_PARENDERECHA   =r'\)'
t_DOLAR          =r'\$'
t_PUNTOYCOMA     =r';'
t_PUNTO          =r'\.'
t_COMA           =r','
t_DOSPUNTOS      =r':'
t_LLAVEIZQ       =r'{'
t_LLAVEDER     	 =r'}'
t_CORCHIZQ       =r'\['
t_CORCHDER       =r'\]'
t_AMPERSAND      =r'\&'
t_PLUS           =r'\+'
t_MINUS          =r'-'
t_DIVIDE         =r'/'
t_MULTI          =r'\*'
t_MENORQ         =r'<'
t_MAYORQ         =r'>'
t_IGUAL          =r'='
t_LOGNEGACION    =r'\!'
#t_TAB			=r'\t'
#t_ESP			=r'\s'



def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_MINUSMINUS(t):
	r'--'
	return t

def t_IQUALIQUAL(t):
	r'=='
	return t

def t_DIFERENTE(t):
	r'!='
	return t

def t_IF(t):
	r'if'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_DO(t):
	r'do'
	return t

def t_WHILE(t):
	r'while'
	return t



def t_FOR(t):
	r'for'
	return t

def t_SWITCH(t):
	r'switch'
	return t

def t_CASE(t):
	r'case'
	return t



def t_LOGAND(t):
	r'and'
	return t

def t_LOGOR(t):
	r'or'
	return t

def t_LOGY(t):
	r'\&\&'
	return t

def t_LOGXOR(t):
	r'xor'
	return t

def t_BREAK(t):
	r'break'
	return t

def t_CONTINUE(t):
	r'continue'
	return t

def t_DEFAULT(t):
	r'default'
	return t

def t_INICIO(t):
	r'<\?php'
	return t

def t_FIN(t):
	r'\?>'
	return t



def t_GLOBAL(t):
	r'global'
	return t

def t_STATIC(t):
	r'static'
	return t

def t_CONST(t):
	r'const'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_FUNCTION(t):
	r'function'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_NULL(t):
	r'null'
	return t

def t_CLASS(t):
	r'class'
	return t

def t_PUBLIC(t):
	r'public'
	return t

def t_PRIVATE(t):
	r'private'
	return t

def t_NEW(t):
	r'new'
	return t

def t_EXTENDS(t):
	r'extends'
	return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t



#TENGO DUDAS SOBRE EL ID
def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t
'''
def t_SALTO(t):
    r'\n'
    return t
'''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

#--------------------------------

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()


#Funcion para recibir la operacion a calcular y
#definir donde hay errores lexicos segun los caracteres ingresados
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba2.c'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()
