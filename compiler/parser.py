# parser.py
import ply.lex as lex
import ply.yacc as yacc

tokens = ('OR', 'AND')

t_AND = r'\&'
t_OR = r'\|'
t_NUMBER = r'\d+'
t_ignore = ' \t'

def t_error(t):
    print("Caractère illégal:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression_and(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_or(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_error(p):
    print("Erreur de syntaxe", p)

parser = yacc.yacc()

if __name__ == "__main__":
    import sys
    code = open(sys.argv[1]).read()
    result = parser.parse(code)
    print("Résultat :", result)
