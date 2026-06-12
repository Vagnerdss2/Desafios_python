"""
1.	Calculadora Básica de Terminal: Um programa que pede dois números e a operação (+, -, *, /).
 Use condicionais para validar a operação e um laço while para manter a calculadora rodando até o usuário decidir sair.
"""

while True:
    print("#" * 30)
    print("Calculadora de terminal.")
    print("#" * 30)


    num1 = int(input("Escolha o primeiro numero: "))
    num2 = int(input("Escolha o segundo numero: "))


    print("=" * 30)
    print("1 - Somar")
    print("2 - Diminuir")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("=" * 30)

    operacao = int(input("Agora escolha a operação: "))



    if operacao == 1:
        soma = num1 + num2
        print(f'O resultado da soma é: {soma}')

    elif operacao == 2:
        diminuir = num1 - num2
        print(f'O resultado da subtração é: {diminuir}')

    elif operacao == 3:
        multiplicar = num1 * num2
        print(f'O resultado da multiplicação é: {multiplicar}')

    elif operacao == 4:
        dividir = num1 / num2
        print(f'O resultado da divisão é: {dividir}')

    elif operacao == 5:
        print("Até a próxima!!")
        break
    else:
        print("Operação inválida")
        print("=" * 30)





