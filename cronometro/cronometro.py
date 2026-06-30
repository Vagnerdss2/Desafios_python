'''
Cronômetro/Temporizador Regressivo: O usuário digita o tempo em segundos,
e o script faz uma contagem regressiva no terminal usando time.sleep(1
'''
import time

segundos = int(input("Digite o tempo em segundos: "))


for i in range(segundos,0,-1):
    time.sleep(1)
    print(i)