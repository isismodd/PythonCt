def exibir_menu():
    """Exibe o menu principal com as opções disponíveis"""
    print("\n" + "="*50)
    print("MENU PRINCIPAL".center(50))
    print("="*50)
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Buscar item na lista")
    print("4. Listar todos os itens")
    print("5. Falar com o suporte")
    print("6. Sair")
    print("="*50)

def validar_opcao(opcoes_validas):
    """
    Valida a entrada do usuário para garantir que é uma opção válida do menu
    Parâmetros:
        opcoes_validas (list): Lista de opções válidas
    Retorna:
        int: Opção válida escolhida pelo usuário
    """
    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao in opcoes_validas:
                return opcao
            else:
                print(f"Opção inválida! Digite um número entre {min(opcoes_validas)} e {max(opcoes_validas)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

def adicionar_item(lista):
    """
    Adiciona um item à lista após validação
    Parâmetros:
        lista (list): Lista onde o item será adicionado
    Retorna:
        list: Lista atualizada
    """
    item = input("Digite o item a ser adicionado: ").strip()
    if item:
        lista.append(item)
        print(f"Item '{item}' adicionado com sucesso!")
    else:
        print("Erro: Não é possível adicionar um item vazio.")
    return lista

def remover_item(lista):
    """
    Remove um item da lista após validação
    Parâmetros:
        lista (list): Lista de onde o item será removido
    Retorna:
        list: Lista atualizada
    """
    if not lista:
        print("A lista está vazia. Nada para remover.")
        return lista
    
    print("Itens na lista:")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    
    while True:
        try:
            indice = int(input("Digite o número do item a ser removido: ")) - 1
            if 0 <= indice < len(lista):
                item_removido = lista.pop(indice)
                print(f"Item '{item_removido}' removido com sucesso!")
                return lista
            else:
                print(f"Índice inválido! Digite um número entre 1 e {len(lista)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

def buscar_item(lista):
    """
    Busca um item na lista e mostra sua posição
    Parâmetros:
        lista (list): Lista onde será feita a busca
    """
    if not lista:
        print("A lista está vazia. Nada para buscar.")
        return
    
    termo = input("Digite o termo de busca: ").strip().lower()
    if not termo:
        print("Termo de busca não pode ser vazio.")
        return
    
    encontrados = [(i, item) for i, item in enumerate(lista, 1) if termo in item.lower()]
    
    if encontrados:
        print("Itens encontrados:")
        for i, item in encontrados:
            print(f"{i}. {item}")
    else:
        print("Nenhum item encontrado com o termo fornecido.")

def listar_itens(lista):
    """
    Lista todos os itens da lista com suas posições
    Parâmetros:
        lista (list): Lista a ser exibida
    """
    if not lista:
        print("A lista está vazia.")
        return
    
    print("\nITENS NA LISTA:")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")
    print(f"Total de itens: {len(lista)}")

def falar_com_suporte():
    """
    Coleta a mensagem do usuário para o suporte e confirma o envio
    Retorna:
        str: A mensagem enviada ao suporte (para fins de demonstração)
    """
    print("\nFALAR COM O SUPORTE")
    print("Digite sua mensagem de ajuda abaixo (Pressione 'fim' em uma linha separada para terminar):")
    
    mensagem = []
    while True:
        linha = input().strip()
        if linha.lower() == 'fim':
            break
        mensagem.append(linha)
    
    mensagem_completa = "\n".join(mensagem)
    
    if mensagem_completa:
        print("\nMensagem enviada ao suporte:")
        print("-"*50)
        print(mensagem_completa)
        print("-"*50)
        print("Seu pedido de ajuda foi enviado ao suporte com sucesso!")
        print("Entraremos em contato em breve.")
    else:
        print("Nenhuma mensagem foi digitada. O pedido de ajuda foi cancelado.")
    
    return mensagem_completa

def main():
    """Função principal que gerencia o fluxo do programa"""
    lista_itens = []
    opcoes_validas = range(1, 7)
    
    while True:
        exibir_menu()
        opcao = validar_opcao(opcoes_validas)
        
        if opcao == 1:
            lista_itens = adicionar_item(lista_itens)
        elif opcao == 2:
            lista_itens = remover_item(lista_itens)
        elif opcao == 3:
            buscar_item(lista_itens)
        elif opcao == 4:
            listar_itens(lista_itens)
        elif opcao == 5:
            falar_com_suporte()
        elif opcao == 6:
            print("Saindo do programa... Até logo!")
            break
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
