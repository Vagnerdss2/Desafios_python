'''
Analisador de Textos (Contador de Palavras): O usuário digita um parágrafo e o script retorna o número total de palavras,
 a quantidade de vogais e qual a palavra mais longa.
'''

frase = input("Digite uma frase: ")

#total de palavras
palavras = frase.split(" ")
total_palavras = len(palavras)
print(f'Temos um total de {total_palavras} palavras')

#quantidade de vogais
qtd_vogais = sum(frase.count(vogal) for vogal in "aeiouáàãéèêãóõ")
print(f"Total de vogais: {qtd_vogais}")

#Palavra mais longa
maior_palavra = ""
tamanho_maximo = 0
for palavra in palavras:
    if len(palavra) > tamanho_maximo:
        tamanho_maximo = len(palavra)
        maior_palavra = palavra
print(f'A maior palavra é {maior_palavra}')


