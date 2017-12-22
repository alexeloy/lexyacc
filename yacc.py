
def p_error(p):
    if p:
        print ("Error on %s" % p.value)
    else:
        print ("Error")

def p_statement(p):
    '''
    statement : select search from identifier where condition
    '''
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
    print ("Sintax are correct") # Se ele reconhecer a sintaxe, sera impresso isto para confirmar


def p_select(p):
    '''
    select : SELECT
    '''
    p[0] = p[1]


def p_search(p):
    '''
    search : identifier
           | TIMES
    '''
    p[0] = p[1]

def p_from(p):
    '''
    from : FROM
    '''
    p[0] = p[1]

def p_where(p):
    '''
    where : WHERE
    '''
    p[0] = p[1]


def p_condition(p):
    '''
    condition : condition_equal
              | condition OR condition
              | condition AND condition
    '''
    if len(p) == 2:  # Para quando nao usa a expressao OR ou AND
        p[0] = p[1]
    elif len(p) == 4: # Para quando e utilizado condition OR condition ou condition AND condition
        p[0] = (p[1], p[2], p[3])


def p_condition_equal(p): # Este e um auxiliar para as pesquisas como name='uepb' ou surname='compiladores'
    '''
    condition_equal : identifier EQUAL QUOT identifier QUOT
    '''
    # Ele vai verificar as aspas, porem nao ira retornar-las, pois elas nao precisam fazer parte do termo, apenas na analise
    p[0] = (p[1], p[2], p[3])

def p_identifier(p):
    '''
    identifier : ID
    '''
    p[0] = p[1]

import ply.yacc as yacc
import lex

tokens = lex.tokens
parser = yacc.yacc()

while True:
    try:
        data = raw_input("input-> ")


    except EOFError:
        break
    parser.parse(data)