# Desenvolva um programa que recebe do usuário nome 
# completo e ano de nascimento que seja entre 1922 
# e 2021.

# A partir dessas informações, o sistema mostrará o 
# nome do usuário e a idade que completou, ou completará, 
# no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido 
# no campo do ano, o sistema informará o erro e continuará 
# perguntando até que um valor correto seja preenchido.

def cadastro():
    while True:
        try:
            print("Primeiro Nome: ")
            primeiroNome = str(input())
            print("Segundo Nome: ")
            segundoNome = str(input())
            print("Insira sua data de Nascimento")
            print("Dia: ")
            dia = int(input())
            print("Mes: ")
            mes = int(input())
            print("Ano")
            ano = int(input())
            if primeiroNome != "" and segundoNome != "":
                if dia >= 1 and ano <= 31 or mes >= 1 and mes <= 12:
                    if ano == 0:
                        ano = 2023
                        print("Seu nome é: ", primeiroNome, segundoNome)
                        print("Sua data de nascimento é: ", dia, "/",mes,"/",ano)
                        break
                else: 
                    print("Os campos Dia e Mês devem maiores que 0!")
            else:
                print("Os campos Nome e Sobrenome são obrigatórios.")
                                
        except Exception as e:
            print(e)
            
cadastro()    
    
    
    
