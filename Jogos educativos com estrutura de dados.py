import random
import time


# lista de perguntas sobre equacoes do segundo grau
# cada item e uma tupla com a pergunta e a resposta certa
equacoes = [
    ("A soma de dois numeros e 17 e o produto e 72. Qual e o maior numero?", 9),
    ("As raizes de uma equacao tem soma 15 e produto 56. Qual e a menor raiz?", 7),
    ("Determine a maior raiz da equacao x^2 - 13x + 40 = 0.", 8),
    ("Determine a menor raiz da equacao x^2 - 17x + 72 = 0.", 8),
    ("O produto de dois numeros consecutivos e 72. Qual e o maior deles?", 9),
    ("A soma de dois numeros e 19 e o produto e 88. Qual e o menor numero?", 8),
    ("Determine a soma das raizes da equacao x^2 - 23x + 126 = 0.", 23),
    ("Determine o produto das raizes da equacao x^2 - 21x + 110 = 0.", 110),
    ("A diferenca entre dois numeros e 1 e o produto e 72. Qual e o maior?", 9),
    ("Determine a maior raiz da equacao x^2 - 15x + 54 = 0.", 9)
]

# perguntas sobre funcoes matematicas
funcoes = [
    ("Uma funcao e definida por f(x)=2x^2-5x+3. Calcule f(7).", 66),
    ("Uma funcao e definida por f(x)=3x^2-2x+1. Calcule f(5).", 66),
    ("Uma funcao associa a cada x o valor x^2+4x-3. Qual e a imagem de 8?", 93),
    ("Considere f(x)=2x^2+x-4. Determine f(6).", 74),
    ("Se f(x)=3x^2+2x+5, qual e o valor de f(4)?", 61),
    ("Uma funcao e dada por f(x)=x^2-7x+10. Calcule a imagem de 9.", 28),
    ("Considere f(x)=4x^2-3x+2. Determine f(5).", 87),
    ("Uma funcao e dada por f(x)=2x^2+6x+1. Qual e a imagem de 7?", 141),
    ("Calcule f(6) para a funcao f(x)=x^2+8x+7.", 91),
    ("Considere f(x)=5x^2-4x+3. Determine f(4).", 67)
]

# perguntas sobre polinomios
polinomios = [
    ("Considere P(x)=2x^3-5x^2+4x+1. Determine P(3).", 22),
    ("Considere P(x)=3x^3-2x^2+x+7. Determine P(2).", 25),
    ("Calcule P(4) para P(x)=x^3+2x^2-3x+5.", 81),
    ("Determine P(3) para P(x)=4x^3-x^2+2x-1.", 110),
    ("Qual e o grau do polinomio 8x^8+3x^4+2x+1?", 8),
    ("Qual e o coeficiente lider do polinomio 9x^7+5x^2+4?", 9),
    ("Calcule P(2) para P(x)=x^4-3x^2+2.", 6),
    ("Determine P(3) para P(x)=2x^4-x^3+5.", 140),
    ("Qual e o grau do polinomio 7x^9+x^4+1?", 9),
    ("Qual e o coeficiente lider do polinomio 12x^5+3x^2+8?", 12)
]

# os tres chefes do jogo, cada um com nome, hp e quanto de dano causa
chefes = [
    {"nome": "Ornstein e Soma", "hp": 10, "ataque": 50},
    {"nome": "Sif, o Grande Lobo Seno", "hp": 10, "ataque": 50},
    {"nome": "Gwyn, Senhor dos Senos", "hp": 10, "ataque": 100}
]


# cria o dicionario do jogador com hp inicial 100
def criar_jogador():
    jogador = {"hp": 100, "hp_max": 100}
    return jogador


# mostra a tela de titulo
def exibir_titulo():
    print("=" * 40)
    print("           MATH SOULS")
    print("      Prepare to die edition")
    print("=" * 40)


# mostra o hp do jogador e quantas perguntas faltam pro chefe morrer
def exibir_status(jogador, chefe):
    print("\n--------------------")
    print(f"HP: {jogador['hp']} / {jogador['hp_max']}")
    print(f"Perguntas restantes: {chefe['hp']}")
    print("--------------------")


# le a resposta do usuario e garante que seja um numero inteiro
# fica repetindo ate o usuario digitar algo valido
def ler_resposta():
    while True:
        entrada = input("Sua resposta: ")

        valido = True

        if entrada == "" or entrada == "-":
            valido = False
        else:
            inicio = 0

            if entrada[0] == "-":
                inicio = 1

            for i in range(inicio, len(entrada)):
                if entrada[i] not in "0123456789":
                    valido = False

        if valido:
            return int(entrada)

        print("Digite somente numeros inteiros!")


# processa o que acontece quando o jogador acerta
# chefe perde 1 hp, e se conseguir responder em 1 min o jogador ganha 5 de hp de bonus
def processar_acerto(jogador, chefe, tempo_resposta):
    chefe["hp"] -= 1
    print("\nCERTO!")
    print(f"Faltam {chefe['hp']} perguntas para derrotar o chefe.")

    # bonus de velocidade se respondeu em menos de 1 min
    if tempo_resposta <= 60:
        jogador["hp"] += 5
        if jogador["hp"] > jogador["hp_max"]:
            jogador["hp"] = jogador["hp_max"]
        print("+5 HP de bonus por resposta rapida!")


# processa o que acontece quando o jogador erra
# jogador leva dano igual ao ataque do chefe
def processar_erro(jogador, chefe, resposta_certa):
    jogador["hp"] -= chefe["ataque"]

    # hp nao pode ficar negativo
    if jogador["hp"] < 0:
        jogador["hp"] = 0

    print("\nERRADO!")
    print(f"A resposta certa era: {resposta_certa}")
    print(f"Voce levou {chefe['ataque']} de dano.")


# executa uma rodada: mostra a pergunta, cronometra e verifica a resposta
def realizar_turno(jogador, chefe, lista_perguntas):
    # escolhe uma pergunta aleatoria sem remover da lista
    pergunta, resposta_certa = random.choice(lista_perguntas)

    print("\n>>> DESAFIO <<<")
    print(pergunta)

    # cronometra o tempo de resposta
    inicio = time.time()
    resposta_usuario = ler_resposta()
    tempo_gasto = time.time() - inicio

    if resposta_usuario == resposta_certa:
        processar_acerto(jogador, chefe, tempo_gasto)
    else:
        processar_erro(jogador, chefe, resposta_certa)


# calcula o ranking final baseado no tempo total da partida
def calcular_ranking(segundos):
    if segundos <= 300:
        return "S"
    elif segundos <= 400:
        return "A"
    elif segundos <= 500:
        return "B"
    elif segundos <= 600:
        return "C"
    return "D"


# mostra a tela de vitoria com tempo e ranking
def exibir_vitoria(tempo_total, ranking):
    print("\n==============================")
    print("VOCE DERROTOU TODOS OS CHEFES!")
    print("==============================")
    print(f"Tempo total: {tempo_total} segundos")
    print(f"Ranking: {ranking}")


# embaralha as listas de perguntas e retorna as tres prontas pra usar
def preparar_perguntas():
    # cria novas listas a partir das originais pra nao bagunçar o banco de dados
    lista_eq = list(equacoes)
    lista_func = list(funcoes)
    lista_poli = list(polinomios)

    random.shuffle(lista_eq)
    random.shuffle(lista_func)
    random.shuffle(lista_poli)

    return [lista_eq, lista_func, lista_poli]


# funcao principal que roda o jogo inteiro
# recebe a lista de chefes como parametro
def jogar(lista_chefes):
    inicio_run = time.time()

    exibir_titulo()

    jogador = criar_jogador()
    listas = preparar_perguntas()

    # loop pelos chefes, cada um tem sua lista de perguntas
    for i in range(len(lista_chefes)):

        # cria um dicionario novo com os dados do chefe atual
        chefe_atual = {
            "nome": lista_chefes[i]["nome"],
            "hp": lista_chefes[i]["hp"],
            "ataque": lista_chefes[i]["ataque"]
        }

        print(f"\n=== {chefe_atual['nome']} apareceu! ===")
        time.sleep(1)

        # batalha continua enquanto os dois tiverem hp
        while jogador["hp"] > 0 and chefe_atual["hp"] > 0:
            exibir_status(jogador, chefe_atual)
            realizar_turno(jogador, chefe_atual, listas[i])

        # verifica se o jogador morreu
        if jogador["hp"] <= 0:
            print("\nVOCE MORREU")
            return

        print(f"\n{chefe_atual['nome']} foi derrotado!")
        time.sleep(1)

    # chegou aqui, derrotou tudo
    tempo_total = int(time.time() - inicio_run)
    ranking = calcular_ranking(tempo_total)
    exibir_vitoria(tempo_total, ranking)


# inicia o jogo
jogar(chefes)