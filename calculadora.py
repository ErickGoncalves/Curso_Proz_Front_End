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

# Está primeira calculador tem apenas a função dos operadores de uma caludadora básica!

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


# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
1# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, 
# um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o 
# usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar 
# o resultado. 

# Essa calculadora tem a função dos operadores básicos de uma calculadora, além da opção de sair.

def calculadora(num1, num2, operacao):
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
            res = operacao
    else:
        print("Operação inválida")
        res = operacao

    return res    

while True:
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 0 - Sair): "))

    if operacao == 0:
        print("Saindo...")
        break
    elif operacao > 0 and operacao <= 4 :
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, operacao) #chamada da função

        print("Resultado:", resultado)# imprimindo o resultado.

    else:
        print("Opção inválida")
