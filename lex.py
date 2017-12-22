
# Definindo os tokens

tokens = [
    'ID',
    'TIMES', # Sinal multiplicador ou *
    'EQUAL', # Sinal de igual
    'QUOT',  # Sinal de Aspas
]

reserved_words = {
    'select' : 'SELECT',
    'from' : 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',

}

tokens += list(reserved_words.values())


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Unknown text at %s" % (t.type))

t_TIMES = r'\*'
t_EQUAL = r'\='
t_QUOT = r'\''

t_ignore = ' \t' # Para ignorar os caracteres TAB e VAZIO

import ply.lex as lex
lexer = lex.lex()
