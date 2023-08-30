# Atividade:

# utilizando o colab:
# criem um array para testar a função
# apresentar o elemento
#  como reposta final da função, indicando se ele existe dentro do array procurado ou não.

# Desafio extra:

# adicionem o elemento procurado como uma resposta de interação do usuário. (Input)

# Desafio extra:

# implementar para a função volte ao inicio , caso o elemento procurado não seja encontrado.
# Criar uma função que verifique sua um determinado elemento existe dentro de um array.


lista_de_compras = ['Arroz', 'Feijão', 'Farinha', 'Macarrão'];

def carrinho(array):
        # tamanho = len(array)
        chave = False
        item_selecionado = str(input('Digite o item da lista desejado: ')) #Aqui o código recebe a entrada de Dados

        for i in range(len(array)): #Inicio do loop para que o script encontre o item selecionado dentro do Array

                if array[i] == item_selecionado: # Comparação do Item selecionado com os itens do Array
                    chave = True # Espécie de chave que teve o valor alterado para assim ter o valor utilizado na próxima condição
        if chave: # Verifica se a variável possui o valor verdadeiro
            print('Item econtrado: ',item_selecionado) # Sendo o resultado acima positivo, é mostrado na tela a mendagem entre 'aspas' mais 
            # o item selecionado
        else: # Condição negativa, ou seja, o valor guardado na variável Chave não é verdadeiro ou True.
            print('Item não encontrado: ', item_selecionado) # Mensagem ao Usuário e o item informado por ele
            carrinho(array) # chamando a função novamente, caso caia nesse else para que o usuario digite novamente outra opção
		
        
carrinho(lista_de_compras) # chamando a função para que o programa seja executado.