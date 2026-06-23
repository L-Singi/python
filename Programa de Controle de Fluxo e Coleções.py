import random

# Controle do estoque
estoque = {
    "fone": 20,
    "mouse": 10,
    "teclado": 15,
    "microfone": 10,
    "webcam": 15,
    "monitor": 30,
    "caixa de som": 20,
    "mouse pad": 15,
}

# Histórico das movimentações
historico = []

# Entrada inicial
nome = input("Digite seu nome: ")

# Fluxo principal e menu
while True:
    print("\n*************************")
    print(" MENU ")
    print("*************************")
    print("1. Consultar Estoque")
    print("2. Retirar Item")
    print("3. Ver Histórico")
    print("4. Sair e Sortear")
    opcao = input("Qual opção deseja escolher? ")

    # Consulta de estoque
    if opcao == "1":
        print("\n*************************")
        print(" ESTOQUE ATUAL ")
        print("*************************")
        
        # percorre o dicionário estoque
        for item, quantidade in estoque.items():
            # mostra o produto e a quantidade
            print(f"Produto: {item} | Quantidade: {quantidade}")

    # Retirada de itens
    elif opcao == "2":
        print("\n*************************")
        print(" RETIRAR ITEM ")
        print("*************************")

        # usuário digita o nome do produto
        item = input("Digite o nome do produto: ").lower()

        # verifica se o produto existe
        if item in estoque:

            # usuário digita a quantidade
            quantidade = int(input("Quantos deseja retirar? "))

            # verifica se a quantidade é válida
            if quantidade > 0:

                # verifica se existe estoque suficiente
                if quantidade <= estoque[item]:

                    # diminui a quantidade do estoque
                    estoque[item] -= quantidade

                    # Registro no histórico
                    historico.append(f"{nome} retirou {quantidade} unidade(s) de {item}")

                    # mensagem de sucesso
                    print("\nRetirada realizada com sucesso!")

                    # mostra quanto restou no estoque
                    print(f"Restam {estoque[item]} unidade(s) de {item}")
                else:
                    print("\nQuantidade indisponível no estoque!")
            else:
                print("\nDigite uma quantidade válida!")
        else:
            print("\nProduto não encontrado!")

    # Exibição do histórico
    elif opcao == "3":
        print("\n*************************")
        print(" HISTORICO ")
        print("*************************")

        # verifica se o histórico possui registros
        if len(historico) > 0:

            # percorre a lista do histórico
            for registro in historico:

                # mostra cada movimentação
                print(registro)
        else:
            print("Nenhuma retirada registrada.")

    # Sorteio final
    elif opcao == "4":
        print("\n*************************")
        print(" SORTEIO ")
        print("*************************")

        # verifica se existe histórico para sorteio
        if len(historico) > 0:

            # escolhe uma movimentação aleatória
            sorteado = random.choice(historico)

            # mostra o resultado do sorteio
            print(f"\nO sorteado da rodada, baseado na movimentação '{sorteado}', ganhou um brinde!")
        else:
            print("\nNenhuma movimentação registrada para sorteio.")
        
        # Encerra o programa
        break

    # Controle de erro do menu
    else:
        print("\nOpção inválida! Digite novamente.")

# Fim do sistema
print("\n*************************")
print(" PROGRAMA FINALIZADO ")
