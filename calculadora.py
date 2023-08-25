# Faça uma função calculadora de dois números com três parâmetros: 
# os dois primeiros serão os números da operação e o terceiro será 
# a entrada que definirá a operação a ser executada. Considera a 
# seguinte definição:
# 
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado 
# deverá ser 0.

def calculadora(num1,num2,operacao):
    soma = 1
    subtracao = 2
    mutiplicacao = 3
    divisao = 4
    
    if operacao == 1:
        res = num1 + num2
    elif operacao == 2:
        res = num1 - num2
    elif operacao == 3:
        res = num1 * num2
    elif operacao == 4:
        if num2 != 0:
            res = num1 / num2
        else:
            print("Não é possível dividir um número por zero!")
            res = 0
    return res    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado = calculadora(num1, num2, operacao)
print("Resultado: ", resultado)

