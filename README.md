# Curso de Python

[https://www.youtube.com/playlist?list=PLbIBj8vQhvm2OT4MpkrsKDDVuZ_RlNzli](https://www.youtube.com/playlist?list=PLbIBj8vQhvm2OT4MpkrsKDDVuZ_RlNzli)

## Comentários

```python
'''
Isto é um comentário
'''
# Isto é um comentário
```

## Atribuição

```python
nome = "Pedro Grachet"
```

## Operadores Aritmético

```python
+ #Adição/Contacatenação
- #Subtração
* #Multiplicação
/ #Divisão
// #Divisão com reusltado inteiro
% #Resto da divisão
** #Exponenciação
```

## Variáveis

```python
'''
Nomes de variáveis devem iniciar com uma letra
Nomes de variáveis podem conter números
Nomes compostos podem ser separados por um _
Por conversão, utilize apenas letras minúsculas
'''
nome = 'Luiz Otávio' # string
idade = 25 # int 
altura = 1.80 # float
peso = 100 # int
data_atual = '20/12/2023' # string

```

## Tipos de Dados

```python
inteiro = 5
real = 5.5
booleano = True
texto = '10.5'
#Strings
"Texto com aspas duplas"
'Texto com aspas simples'

print(type(variável)) #Mostrar o tipo da variável
```

## Cast - Conversões

```python
#String para float
texto = '10.5'
texto_float = float(texto)
print(texto_float)

#Float para int
real = 5.9
inteiro = int(real)
```

## Saída de Dados

```python
print() #Comando de saída
print("Hello World!") #Comando de saída com texto
print("Ou qualquer outra coisa", 'qualquer coisa')
print("Texto com \"aspas duplas\" dentro de aspas duplas")
print('Texto com "aspas duplas" dentro de aspas simples')
print(5 + 5)
print("A soma de 5 + 5 é:", 5+5)

# Formatar Número
numero_decimal = 123.3223
numero_decimal = '{:.2f}'.format(numero_decimal)
print(numero_decimal)

print('A variável nome recebeu:', nome)
print('A variável nome recebeu {nome}')
print('A variável nome recebeu {} {}'.format(nome, pedro))
print('A variável nome recebeu {n}'.format(n=nome)) 
print('{0}{0}{0}{0}, tem {1} anos'.format(nome, idade))
print(f'{nome} tem {idade} anos de idade')
```

## Entrada de Dados

```python
nome = str(input("Qual é o seu nome? "))
print(f'O nome digitado pelo usuário é {nome} e a variável é do tipo {type(nome)}')

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
print(f'A soma dos dois números digitados pelo usuário é: {numero1 + numero2}')

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
print(f'A soma dos dois números digitados pelo usuário é: {numero1 + numero2}')
```

## Estruturas Condicionais

```python
#Sintaxe
if condition:
    #true
else:
    #false

#Exemplo
if True:
    print('Verdadeiro')
elif condition:
		print("This condition")
else:
		print("Falso")

```

## Operadores Relacionais

```python
'''Operadores relacionais

==  igual
> maior
>= maior ou igual
< menor
<= menor ou igual
!= diferente
'''
print(1 != '1')
```

## Operadores Lógicos

```python
and -> e
or -> ou
not -> não
in -> Existe
not in -> Não existe

nome = str('Pedro Grachet')
if 'p' in nome:
	print('Contem a letra P no seu nome.')
```

## Formatação de valores

```python
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

num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_1 = 1
print(f'{num_1:0>10}') # Adicionar 9 casas a esquerda do valor 0
print(f'{num_1:2>10}') # Adicionar 9 casas a esquerda do valor 2
print(f'{num_1:2<10}') # Adicionar 10 casas no total a direita com valor 2
print(f'{num_1:2^10}') # Adicionar 10 casas no total a centro com valor 2
print(f'{num_1:0>10.2f}')

nome = 'Pedro Grachet'
print()

#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️
#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️
#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️⚠️
```

## Índices e fatiamento de string

```python
#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️
#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️
#Estudar posteriormenten trabalho com strings⚠️⚠️⚠️⚠️⚠️⚠️
```

## Estruturas de Repetição

```python
#while

while condicao: 
	continue # pula a interação
	pass
	break # quebra o laço
else:
	pass #também pode utilizar o else

# For

texto = 'Python'

for letra in texto:
    print(letra)

texto = 'Python'

for i, letra in enumerate(texto):
    print(i+1, letra)

#Função range(start=0, stop, step=1)

for i in range(10):
    print(i+1)

for i in range(1, 11, 1):
    print(i)
```

## Listas

```python
'''
Listas em python
Para criar lista se utiliza colchetes [ ]

texto = 'valor'
lista = [1, 2, 3, 4, 'Pedrinho', 1.3]
'''

#        0  1  2  3      4        5     -1
lista = [1, 2, 3, 4, 'Pedrinho', 1.3, 10.5]

print(lista[1:4]) #executa do 1 ao 3 (4 não é exibido)
print(lista[:4]) #executa do 0 ao 3 (4 não é exibido)
print(lista[2:]) #executa do 6 ao 3 (2 não é exibido)
print(lista[-1])

#Estudar posteriormenten trabalho listas ⚠️⚠️⚠️⚠️⚠️
#Estudar quando tiver tempo ⚠️⚠️⚠️
# Funçoes Append(), Insert(), Pop(), Del(), Clear(), Extend(), Min(), Max()

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

"""
Desempacotamento de lista em python
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2, n3, *resto_lista = lista
print(n1, n2, resto_lista)
n1, n2, n3, *resto_lista, n4 = lista # pega os 3 primeiros, o meio transforma em uma nova lista e o ultimo elemento da lista
```

## Operador Ternário

```python
"""
Operador Ternário
"""

logged_user = False

# if logged_user:
#     msg = "Usuário logado."
# else:
#     msg = "Usuário precisa logar."

#variable = value if(condition) else value

msg = "Usuário logado." if logged_user else "Usuário precisa logar"

print(msg)

#Other case
idade = 18
e_de_maior = (idade >= 18)
msg = "Pode acessar" if  e_de_maior else "Não pode acessar"
```

## Funções

```python
"""
Funções - pt 1
"""

def funcao(msg):
    print(msg)

def saudacao(msg="Olá", nome="Usuario"):
    print(msg, nome)

funcao("asd")

#Argumento Nomeados
saudacao(nome='Pedro')

"""
Funções - pt 2
"""

def funcao(var):
    print(var)
    
funcao("Valor que eu quero")

def funcao(var):
    return var
    print(var)
    
variavel = funcao("Valor que eu quero")

if variavel:
    print(variavel)
else:
    print("Nenhum valor")

def soma(n1=0, n2=1):
    return n1 + n2

def funccao():
    return soma

#Variável como função
funcaoteste = funccao()

print(type(funcaoteste))

result = funcaoteste(1, 10)
print(result)

"""
Funções - pt 3
"""

def funcao(a1, a2, a3, a4, nome=None, a5=None):
    print(a1, a2, a3, a4, nome, a5)
    return nome, a5

print(funcao(1, 2, 3, 4, "Pedro", "João"))

def func(*args, **kwargs): #*args passa desempacotado numa lista
    # args = list(args)
    # print(args)
    # print(args[1])
    # print(args[-1])
    # for v in args:
    #     print(v)
    # print(kwargs['nome'])
    idade = kwargs['idade'] #Pode gerar exceção se não existir
    nome = kwargs.get('nome') 
    print(nome)
    
    
lista = [1,2,3,4,5]
#n1, n2, *n = lista

func(*lista, nome="Pedro")
```
## Escopo de variáveis de funções

```python
"Escopo de variáveis de funções"

variavel = 'valor' #escopo global

def func():
    print(variavel)
    
def func2():
    global variavel #Nesse caso, da para usar uma variável de escopo global dentro de um escopo menor
    variavel = 'Outro valor'
    print(variavel)

func()
func2()
```
