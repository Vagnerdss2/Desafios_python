'''
2.	Jogo de Adivinhação de Números: O computador escolhe um número aleatório entre 1 e 100 (usando a biblioteca random)
e o usuário tenta adivinhar.
 O programa deve dizer se o palpite foi alto ou baixo e contar o número de tentativas.
'''

import random

numero_aleatorio = random.randint(1,100)

contador = 0

while True:
    numero_usuario = int(input("Escolha um numero de 1 a 100: "))

    if numero_usuario < numero_aleatorio:
        contador += 1
        print("O numero que você escolheu é menor.")
        print(f'{contador}ª tentativa')
    elif numero_usuario > numero_aleatorio:
        contador += 1
        print("O numero que você escolheu é maior.")
        print(f'{contador}ª tentativa')
    elif numero_usuario == numero_aleatorio:
        contador += 1
        print(f'Você acertou, o numéro correto é {numero_usuario}')
        print(f'Você acertou com {contador} tentativas')
        break
    else:
        print('Opção inválida, tente novamente!')
