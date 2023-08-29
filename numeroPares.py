# Problema: Desenvolva um programa que só deve 
# aceitar números pares. Siga as seguintes instruções:

# caso um número ímpar seja digitado, informe 
# ao usuário que ele digitou um valor ímpar e 
# peça novamente por um número par;

# caso uma letra seja digitada, informe ao 
# usuário que ele digitou um caractere inválido 
# e peça novamente por um número par.



def numerosPares():
     
   while True:
    try:
        print("Insira um número")
        valor = int(input())
        if valor % 2 == 0 :
            print ("O valor digitado:", valor," é par, pois possui resto 0.")  
            break      
        else:
            print("O valor digitado:", valor,". NÃO é par, pois possui resto DIFERENTE de 0.")
        
    except Exception as e:
        print(e)
numerosPares()
