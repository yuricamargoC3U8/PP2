import math

print("As operações disponíveis são:  (+, -, *, /).")
n1 = float(input("Digite o primeiro valor: "))
operacao = str(input("Digite sua operação: "))
n2 = float(input("Digite o segundo valor: "))

if operacao == "+":
    print(n1 + n2)
elif operacao == "-":
    print(n1 - n2)
elif operacao == "*":
    print(n1 * n2)
elif operacao == "/":
    print(n1 / n2)
