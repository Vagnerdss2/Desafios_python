'''
Conversor de Unidades Universal: Permita converter temperaturas (Celsius/Fahrenheit),
 distâncias (Metros/Quilômetros/Milhas) e pesos.
'''

print('==== Bem vindo ao conversor Universal de unidades ===')

conversao = int(input('Digite o valor a converter: '))
opcao = int(input('Escolha uma das opções: \n'
      '1 - Celsius -> Fahrenheit \n'
      '2 - Distancias \n'
      '3 - Kilos em gramas:  \n'
        'Digite aqui: '))


if opcao == 1:
   fare = conversao * 1.8 + 32
   print(f'A temperatura em Fahrenheit é {fare}')
elif opcao == 2:
    distancia = float(input('Para qual você quer converter?\n'
          '1 - metros para km \n'
          '2 - metros para milhas: '))
    if distancia == 1:
        km = conversao / 1000
        print(f'O valor convertido em kilômetros é: {km}')
    elif distancia == 2:
        mil = float(conversao * 1.0936)
        print(f'O valor convertido em milhas é: {mil}')
    else:
        print("Opção inválida")
elif opcao == 3:
    peso = conversao * 1000
    print(f'O valor convertido em gramas é: {peso}')
else:
    print("Opção invalida")