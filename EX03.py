#Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
#dois números, a multiplicação, a divisão inteira e o resto da divisão inteira

num1 = int (input("insira o primeiro numero para calcular: "))
num2 = int (input("insira o segundo numero para calcular: "))

print("============================================================")
print("1 - soma\n2-multiplicação\n3-divisão inteira")
print("============================================================")
calculo = int (input("Escolha o tipo de calculo digitando o número correspondente: "))

if calculo == 1:
   print("A soma dos numeros é: ",num1+num2)
elif calculo == 2:
   print("A soma dos numeros é: ",num1*num2)
elif calculo == 3:
   print("A soma dos numeros é: ",num1//num2)
   print("o resto da divisão inteira é: ",(num1%num2))