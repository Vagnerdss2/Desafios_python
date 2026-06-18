'''
Gerador de Senhas Seguras: Um script que pergunta o comprimento da senha desejada e se deve incluir maiúsculas,
números e caracteres especiais, gerando a senha aleatoriamente.
'''

import random
import string

lista_especial = "!@#$%&*"
digitos_especiais = lista_especial + string.digits

senha_usuario = int(input("Qual o tamanho da sua senha, 8 ou 16 caracteres: "))
if senha_usuario == 8 or senha_usuario == 16:
    caracter_especial = input("Deseja cacter especial: S/N: ").lower()

    if senha_usuario == 8 and caracter_especial == "s":
        senha = "".join(random.choices(digitos_especiais, k=senha_usuario))
        print(f'Sua senha é: {senha}')
    if senha_usuario == 8 and caracter_especial == "n":
        senha ="".join( random.choices(string.digits,k=senha_usuario))
        print(f'Sua senha é: {senha}')
    if senha_usuario == 16 and caracter_especial == "s":
        senha = "".join(random.choices(digitos_especiais, k=senha_usuario))
        print(f'Sua senha é: {senha}')
    if senha_usuario == 16 and caracter_especial == "n":
        senha ="".join( random.choices(string.digits,k=senha_usuario))
        print(f'Sua senha é: {senha}')
    else:
        print('Opção inválida!')
else:
    print('Opção inválida!')






