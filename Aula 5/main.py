'''
 Formatando valores com modificadores
 :s - Texto(Strings)
 :d - Inteiros
 :f - Numeros com decimais
 :.(numero)f - quantidade de casas decimais
 :(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
 
 > - esquerda
 < - direita
 ^ - centro
'''

# num1 = 10
# num2 = 3
# divisao = num1 / num2
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

num_1 = 1
print(f'{num_1:0>10}') # Adicionar 10 casas no total a esquerda com valor 0
print(f'{num_1:2^10}') # Adicionar 10 casas no total a centro com valor 2
nome = 'teste'
nome = nome.capitalize()
print(nome)
