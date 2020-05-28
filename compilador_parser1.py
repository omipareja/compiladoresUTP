import ply.yacc as yacc
from compilador import tokens
import compilador
import sys

VERBOSE = 1

'''
PRUEBA
'''
def p_program(p):
	'program : declaration_list'
	pass



def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | operaction_declaration
				  | fun_declaration
				  | header_declaration
				  | class_declaration

				  '''
	pass

def p_class_declaration(p):
	'class_declaration : CLASS IDENTIFICADOR bloque_declaration'
	pass

def p_bloque_declaration(p):
	'''bloque_declaration : LLAVEIZQ bloque_declaration_2 LLAVEDER
							| CLASS IDENTIFICADOR EXTENDS IDENTIFICADOR  bloque_declaration
	'''
	pass

def p_bloque_declaration_2(p):
	''' bloque_declaration_2 : fun_declaration bloque_declaration_2
								| fun_declaration
	 '''
	pass


def p_header_declaration_1(p):
	'header_declaration : INICIO program FIN'
	pass


def p_var_declaration_1(p):
	'var_declaration : type_specifier var_declaration2 PUNTOYCOMA'
	pass

def p_var_declaration_2(p):
	'var_declaration :  type_specifier DOLAR IDENTIFICADOR CORCHIZQ CORCHDER PUNTOYCOMA'
	pass

def p_var_declaration_3(p):
	'''var_declaration2 : DOLAR IDENTIFICADOR COMA var_declaration2
                                    | DOLAR IDENTIFICADOR
                                    | DOLAR IDENTIFICADOR IGUAL NUMERO COMA var_declaration2
                                    | DOLAR IDENTIFICADOR IGUAL NUMERO
									| AMPERSAND IDENTIFICADOR
									| DOLAR IDENTIFICADOR IGUAL NULL
									| CONST IDENTIFICADOR IGUAL NUMERO
        '''
	pass



def p_type_specifier_1(p):
	'type_specifier : PUBLIC'
	pass

def p_type_specifier_2(p):
	'type_specifier : PRIVATE'
	pass


def p_operation_declaration(p):
	'operaction_declaration : statement '
	pass


def p_fun_declaration_1(p):
	'fun_declaration : type_specifier type_function FUNCTION  IDENTIFICADOR PARENIZQUIERDA params PARENDERECHA  compount_stmt  '
	pass

def p_fun_declaration_2(p):
	'fun_declaration : type_specifier type_function FUNCTION AMPERSAND IDENTIFICADOR PARENIZQUIERDA params PARENDERECHA  compount_stmt  '
	pass

def p_type_function_1(p):
	'type_function : STATIC'
	pass

def p_type_function_2(p):
	'type_function : empty'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_param_list_1(p):
	'param_list : param_list COMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : DOLAR IDENTIFICADOR'
	pass

def p_compount_stmt(p):
	'''compount_stmt : LLAVEIZQ local_declarations statement_list LLAVEDER
		| LLAVEIZQ local_declarations statement_list LLAVEDER WHILE PARENIZQUIERDA expression PARENDERECHA PUNTOYCOMA
	'''
	pass




def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| imprimir_pantalla
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
				| continue_stmt
				| object_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression PUNTOYCOMA'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : PUNTOYCOMA'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF PARENIZQUIERDA expression PARENDERECHA statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : IF PARENIZQUIERDA expression PARENDERECHA statement ELSE statement'
	pass

def p_selection_stmt_3(p):
	'selection_stmt : SWITCH PARENIZQUIERDA var_declaration2 PARENDERECHA statement'
	pass

def p_selection_stmt_4(p):
	'selection_stmt : CASE NUMERO DOSPUNTOS statement BREAK PUNTOYCOMA '
	pass

def p_selection_stmt_5(p):
	'selection_stmt : DEFAULT DOSPUNTOS statement BREAK PUNTOYCOMA'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE PARENIZQUIERDA expression PARENDERECHA statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : FOR PARENIZQUIERDA var_declaration2 PUNTOYCOMA expression PUNTOYCOMA additive_expression PARENDERECHA statement'
	pass

def p_iteration_stmt_3(p):
	'iteration_stmt : DO statement'
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN PUNTOYCOMA'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression PUNTOYCOMA'
	pass

def p_continue_stmt(p):
	'continue_stmt : CONTINUE PUNTOYCOMA '
	pass

def p_object_stmt(p):
	' object_stmt : NEW DOLAR IDENTIFICADOR IGUAL IDENTIFICADOR argumento '
	pass

def p_argumento(p):
	' argumento : PARENIZQUIERDA argumento_2 PARENDERECHA PUNTOYCOMA '
	pass

def p_argumento_2(p):
	''' argumento_2 : DOLAR IDENTIFICADOR COMA argumento_2
					 | COMILLA IDENTIFICADOR COMILLA COMA argumento_2
					 | COMILLA IDENTIFICADOR COMILLA
					 | DOLAR IDENTIFICADOR
					 | NUMERO argumento_2
					 | NUMERO

	'''
	pass

def p_imprimir_pantalla(p):
	''' imprimir_pantalla : PRINT COMILLA CADENA COMILLA PUNTOYCOMA
							| PRINT COMILLA CADENA COMILLA PUNTO expression  PUNTOYCOMA
							|  PRINT COMILLA CADENA COMILLA PUNTO expression PUNTO COMILLA CADENA COMILLA  PUNTOYCOMA
	'''
	pass

def p_cadenas(p):
	''' CADENA : IDENTIFICADOR CADENA
				| NUMERO CADENA
				| NUMERO
				| IDENTIFICADOR
	'''
	pass

def p_expression_1(p):
	'expression : var_declaration2 IGUAL expression'
	pass


def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var_declaration2 IGUAL  var_declaration2 PUNTOYCOMA'
	pass



def p_simple_expression_1(p):
	'''simple_expression : additive_expression relop additive_expression
						| additive_expression relop additive_expression relop additive_expression
						| additive_expression relop additive_expression relop additive_expression relop additive_expression
						| additive_expression relop additive_expression relop additive_expression relop additive_expression relop additive_expression
	'''
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass

def p_relop(p):
	'''relop : MENORQ
			|  MAYORQ
			| DIFERENTE
			| LOGNEGACION
			| IQUALIQUAL
			| LOGOR
			| LOGXOR
			| LOGAND
			| LOGY
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term

        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term MINUSMINUS'
	pass

def p_additive_expression_4(p):
	'additive_expression : term PLUSPLUS'
	pass

def p_addop(p):
	'''addop : PLUS
			| MINUS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_mulop(p):
	'''mulop : 	MULTI
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : PARENIZQUIERDA expression PARENDERECHA'
	pass

def p_factor_2(p):
	'factor : var_declaration2'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMERO'
	pass

def p_call(p):
	'call : DOLAR IDENTIFICADOR PARENIZQUIERDA args PARENDERECHA'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass
#--------------------------------------------------------------------------
def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba2.c'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input()
