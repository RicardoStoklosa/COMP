from class_DFA import DFA
from utils import *

const = DFA(*read_quintuple_from_data("const"))
soma = DFA(*read_quintuple_from_data("soma"))
subtracao = DFA(*read_quintuple_from_data("subtracao"))
multiplicacao = DFA(*read_quintuple_from_data("multiplicacao"))
divisao = DFA(*read_quintuple_from_data("divisao"))

data = [ i for i in input("Digite a expressão").split() ]

exp = {}

for word in data:
    if const.run_with_word(word):
        exp[word] = 'constante'
    elif soma.run_with_word(word):
        exp[word] = 'soma'
    elif subtracao.run_with_word(word):
        exp[word] = 'subtração'
    elif multiplicacao.run_with_word(word):
        exp[word] = 'multiplicação'
    elif divisao.run_with_word(word):
        exp[word] = 'divisão'
    else:
        exp[word] = 'não reconhecido'

for word in data:
    print(word,':',exp[word])