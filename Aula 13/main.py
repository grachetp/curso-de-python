"""
Split, Join e Enumerate
Split - Dividi uma string gerando uma lista
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # list
"""

variavel = 'texto'
variavel.split(",").sort()
variavel.join("jabuticaba")

variavel = ','.join(variavel)

# Pega a posição do valor e imprime do valor
for indice, valor in enumerate(variavel):
    print(indice, valor)
    
lista = [
    [1, 3],
    [2, 4],
    [5, 5]
]
