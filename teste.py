#Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
#algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim
#de 2024. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
#programa deverá imprimir:
#Fulano de tal tem (ou terá) 34 anos

import datetime

x = datetime.datetime.now()
nome = input("insira seu nome: ")

anoNasc = int (input("Insira o ano do seu nascimento: "))

idade = (x.year - anoNasc)

print (nome," tem ou terá",idade," anos esse ano")