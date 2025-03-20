#Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
#dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
#divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

num = int (input("Insira um numero inteiro de 0 a 99: "))

unidade = (num %10)
dezena = (num - unidade)//10

print("A unidade desse numero é: ",unidade,"e a dezena é",dezena)
