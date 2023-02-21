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
