# -*- coding: utf-8 -*-

# Aula 1, Exercício 1
# Trecho de código responsável por trocar o valor de quatro variáveis
w = 1
x = 2
y = 3
z = 4

# Versão multilinha
aux = w
w = z
z = aux
aux = x
x = y
y = aux

# Versão uma linha
w, x, y, z = z, y, x, w


def imprimir_sequencia(n):
    """
    Aula 1, Exercício 2

    Função que recebe um número n e escreve o seguinte na tela:

        1
        2 2
        3 3 3
        ...
        n n n n n n ... n
    """
    i = 1
    while i <= n:
        j = 0
        while j < i:
            print i,
            j += 1
        print
        i += 1

def imprimir_na_vertical(palavra):
    """
    Aula 1, Exercício 3

    Função que recebe uma palavra e escreve ela na vertical.

    Exemplo de entrada: Chico
    Exemplo de saída:
        C
        h
        i
        c
        o
    """
    for letra in palavra:
        print letra

def listar_pares(n):
    """
    Aula 1, Exercício 4

    Função que recebe um número n e retorna uma lista com todos os pares entre 1 e n,
    incluindo n, caso o mesmo seja par.

    Implementação no modelo Java de ser.

    Alternativas de uma linha de código:

        >>> range(2, n + 1, 2)

    Ou ainda, com list comprehension:

        >>> [ numero for numero in range(1, n + 1) if x % 2 == 0 ]

    Ou ainda, com filter + lambda:

        >>> filter(lambda x: x % 2 == 0, range(1, n + 1))
    """
    lista_pares = []
    lista = range(1, n + 1)
    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

def escrever_chave_valor_dicionario(dicionario):
    """
    Aula 1, Exercício 5

    Função que recebe um dicionário e escreve as chaves e os valores em pares:

        <chave> : <valor>"""
    for chave, valor in dicionario.items():
        print '%s : %s' % (chave, valor)
