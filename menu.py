def exibir_menu():
    """Exibe o menu principal com as opções disponíveis"""
    print("\n" + "="*50)
    print("MENU PRINCIPAL".center(50))
    print("="*50)
    print("1. Solicitar senha para atendimento")
    print("2. Solicitar tutorial de login")
    print("3. Solicitar tutorial de chamada")
    print("4. Solicitar chat com o médico (durante consulta, em caso de problemas)")
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

def solicitar_senha():
    """Gera uma senha de atendimento fictícia"""
    import random
    senha = f"P-{random.randint(1000, 9999)}"
    print(f"\nSenha de atendimento gerada: {senha}")
    print("Por favor, aguarde sua vez no sistema.")

def tutorial_login():
    """Exibe um tutorial passo a passo para login"""
    print("\nTUTORIAL DE LOGIN:")
    print("1. Baixe o aplicativo da clínica.")
    print("2. Clique no botão 'ENTRAR' no centro da tela.")
    print("3. Insira seu CPF.")
    print("4. Clique em 'Entrar'.")

def tutorial_chamada():
    """Exibe um tutorial passo a passo para iniciar uma chamada"""
    print("\nTUTORIAL DE CHAMADA:")
    print("1. Faça entrada no sistema.")
    print("2. Na página inicial, clique em 'Iniciar Chamada'.")
    print("3. Permita o acesso ao microfone e câmera quando solicitado.")
    print("4. Aguarde a conexão com o médico.")
    print("5. Em caso de falha, reinicie o navegador ou aplicativo.")

def chat_com_medico():
    """Simula a abertura de um chat com o médico durante a consulta"""
    print("\nSOLICITANDO CHAT COM O MÉDICO...")
    print("Conectando você ao médico responsável...")
    print("(Este chat só está disponível durante consultas ativas.)")
    print("Se não estiver em consulta, contate o suporte técnico.")

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
    opcoes_validas = range(1, 7)
    
    while True:
        exibir_menu()
        opcao = validar_opcao(opcoes_validas)
        
        if opcao == 1:
            solicitar_senha()
        elif opcao == 2:
            tutorial_login()
        elif opcao == 3:
            tutorial_chamada()
        elif opcao == 4:
            chat_com_medico()
        elif opcao == 5:
            falar_com_suporte()
        elif opcao == 6:
            print("Saindo do programa... Até logo!")
            break
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
