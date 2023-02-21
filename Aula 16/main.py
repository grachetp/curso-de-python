# """
# Funções - pt 1
# """

# def funcao(msg):
#     print(msg)

# def saudacao(msg="Olá", nome="Usuario"):
#     print(msg, nome)

# funcao("asd")

# #Argumento Nomeados
# saudacao(nome='Pedro')

# """
# Funções - pt 2
# """

# def funcao(var):
#     print(var)
    
# funcao("Valor que eu quero")

# def funcao(var):
#     return var
#     print(var)
    
# variavel = funcao("Valor que eu quero")

# if variavel:
#     print(variavel)
# else:
#     print("Nenhum valor")

# def soma(n1=0, n2=1):
#     return n1 + n2

# def funccao():
#     return soma

# #Variável como função
# funcaoteste = funccao()

# print(type(funcaoteste))

# result = funcaoteste(1, 10)
# print(result)

# """
# Funções - pt 3
# """

# def funcao(a1, a2, a3, a4, nome=None, a5=None):
#     print(a1, a2, a3, a4, nome, a5)
#     return nome, a5

# print(funcao(1, 2, 3, 4, "Pedro", "João"))

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
