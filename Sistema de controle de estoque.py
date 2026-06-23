# mostra o menu principal na tela
def exibir_menu():
    print("\n=============================")
    print("  CONTROLE DE ESTOQUE")
    print("=============================")
    print("1 - Cadastrar produto")
    print("2 - Pesquisar produto")
    print("3 - Listar produtos")
    print("4 - Atualizar produto")
    print("0 - Sair")
    print("=============================")


# lê a opção do menu, se digitar letra não deixa o programa travar
def ler_opcao():
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
        else:
            return opcao
        finally:
            print("[LOG] Tentativa de leitura de opção registrada.")


# cadastra um novo produto no dicionário estoque
def cadastrar_produto(estoque):
    print("\n--- CADASTRO DE PRODUTO ---")

    # vai ler o ID e garantir que é um número positivo
    while True:
        try:
            id_produto = int(input("Escreva o ID do produto: "))
            if id_produto <= 0:
                raise ValueError("O ID do produto deve ser um número positivo!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            break
        finally:
            print("[LOG] Tentativa de leitura de ID registrada.")

    # verifica se já existe um produto com esse ID
    if id_produto in estoque:
        print("Erro: já existe um produto com esse ID!")
        return

    # lê o nome e exige pelo menos 3 caracteres
    while True:
        try:
            nome = input("Nome do produto: ")
            if len(nome) < 3:
                raise ValueError("O nome do produto deve ter pelo menos 3 caracteres!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            break
        finally:
            print("[LOG] Tentativa de entrada de nome registrada.")

    # lê a quantidade e exige que seja maior que zero
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            break
        finally:
            print("[LOG] Tentativa de entrada de quantidade registrada.")

    # lê o preço e verifica se está dentro dos limites permitidos
    while True:
        try:
            preco = float(input("Preço unitário (R$): "))
            if preco <= 0:
                raise ValueError("O preço deve ser maior que zero!")
            if preco > 10000:
                raise ValueError("O preço não pode ultrapassar R$ 10.000,00!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            print("Validação concluída.")
            break
        finally:
            print("[LOG] Tentativa de entrada de preço registrada.")

    # salva o produto no dicionário com os dados informados
    estoque[id_produto] = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    print(f'Produto "{nome}" cadastrado com sucesso!')


# busca um produto pelo ID e exibe os dados dele
def pesquisar_produto(estoque):
    print("\n--- PESQUISAR PRODUTO ---")

    # lê o ID para pesquisa com proteção contra letras
    while True:
        try:
            id_pesquisa = int(input("Digite o ID do produto que procura: "))
        except ValueError:
            print("Digite somente números para ID!")
        else:
            break
        finally:
            print("[LOG] Tentativa de leitura de ID registrada.")

    # tenta acessar o produto no dicionário, se não existir cai no KeyError
    try:
        produto = estoque[id_pesquisa]
    except KeyError:
        print("Produto não encontrado!")
    else:
        # só exibe os dados se o produto foi encontrado
        print("\n--- PRODUTO ENCONTRADO ---")
        print(f"ID: {id_pesquisa}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
    finally:
        print("[LOG] Pesquisa finalizada.")


# lista todos os produtos cadastrados no estoque
def listar_produtos(estoque):
    print("\n--- LISTA DE PRODUTOS ---")

    # verifica se o estoque está vazio antes de tentar listar
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    for id_produto, produto in estoque.items():
        print("-----------------------------")
        print(f"ID: {id_produto}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")


# altera o nome de um produto já existente
def alterar_nome(produto):
    while True:
        try:
            novo_nome = input("Novo nome: ")
            if len(novo_nome) < 3:
                raise ValueError("O nome deve ter pelo menos 3 caracteres!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            produto["nome"] = novo_nome
            print("Nome atualizado com sucesso!")
            break
        finally:
            print("[LOG] Tentativa de alteração de nome registrada.")


# altera a quantidade de um produto já existente
def alterar_quantidade(produto):
    while True:
        try:
            nova_quantidade = int(input("Nova quantidade: "))
            if nova_quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            produto["quantidade"] = nova_quantidade
            print("Quantidade atualizada com sucesso!")
            break
        finally:
            print("[LOG] Tentativa de alteração de quantidade registrada.")


# altera o preço de um produto já existente
def alterar_preco(produto):
    while True:
        try:
            novo_preco = float(input("Novo preço: "))
            if novo_preco <= 0:
                raise ValueError("O preço deve ser maior que zero!")
            if novo_preco > 10000:
                raise ValueError("O preço não pode ultrapassar R$ 10.000,00!")
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            produto["preco"] = novo_preco
            print("Preço atualizado com sucesso!")
            break
        finally:
            print("[LOG] Tentativa de alteração de preço registrada.")


# mostra o menu de opções de atualização
def exibir_menu_atualizacao():
    print("\n  O que deseja atualizar?")
    print("  1 - Nome")
    print("  2 - Quantidade")
    print("  3 - Preço")
    print("  4 - Tudo")


# atualiza os dados de um produto existente no estoque
def atualizar_produto(estoque):
    print("\n--- ATUALIZAR PRODUTO ---")

    # lê o ID do produto que será atualizado
    while True:
        try:
            id_produto = int(input("Digite o ID do produto: "))
        except ValueError:
            print("Digite somente números!")
        else:
            break
        finally:
            print("[LOG] Leitura do ID realizada.")

    # verifica se o produto existe no dicionário
    try:
        produto = estoque[id_produto]
    except KeyError:
        print("Produto não encontrado!")
    else:
        # só entra aqui se o produto foi encontrado
        exibir_menu_atualizacao()

        # lê a opção de atualização e valida se está entre 1 e 4
        while True:
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha not in (1, 2, 3, 4):
                    raise ValueError("Opção inválida! Escolha entre 1 e 4.")
            except ValueError as erro:
                print(f"Erro: {erro}")
            else:
                break
            finally:
                print("[LOG] Tentativa de leitura de opção de atualização registrada.")

        # chama a função que o usuário escolheu
        if escolha == 1:
            alterar_nome(produto)
        elif escolha == 2:
            alterar_quantidade(produto)
        elif escolha == 3:
            alterar_preco(produto)
        elif escolha == 4:
            alterar_nome(produto)
            alterar_quantidade(produto)
            alterar_preco(produto)

        print("\nProduto atualizado com sucesso!")

    finally:
        print("[LOG] Atualização finalizada.")


# função principal que inicia o sistema
def main():

    # dicionário principal que vai servir como banco de dados em memória
    # a chave é o ID do produto e o valor é outro dicionário com os detalhes
    estoque = {
        101: {"nome": "Camiseta Básica",  "quantidade": 20, "preco": 49.90},
        102: {"nome": "Calça Jeans",       "quantidade": 15, "preco": 129.90},
        103: {"nome": "Vestido Floral",    "quantidade": 8,  "preco": 159.90},
        104: {"nome": "Blusa Cropped",     "quantidade": 12, "preco": 69.90},
        105: {"nome": "Saia Midi",         "quantidade": 10, "preco": 89.90}
    }

    print("Bem-vindo ao sistema de estoque!")

    # laço principal que fica rodando até o usuário escolher sair
    while True:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == 1:
            cadastrar_produto(estoque)
        elif opcao == 2:
            pesquisar_produto(estoque)
        elif opcao == 3:
            listar_produtos(estoque)
        elif opcao == 4:
            atualizar_produto(estoque)
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


main()