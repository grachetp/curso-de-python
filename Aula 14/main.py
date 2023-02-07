"""
Desempacotamento de lista em python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2, n3, *resto_lista = lista
print(n1, n2, resto_lista)
n1, n2, n3, *resto_lista, n4 = lista # pega os 3 primeiros, o meio transforma em uma nova lista e o ultimo elemento da lista
