print('***************************************************')
print(' SISTEMA DE CONTROLE DE VENDAS ')
print('***************************************************')

nome = input('Informe o nome do gestor: ')
mes = input('Informe o mês de referência: ')

# Exibe confirmação do dados informados
print('\nDADOS INFORMADOS')
print('GESTOR:', nome)
print('MÊS DE REFERÊNCIA:', mes)

# Entrada de dados

dias = int(input("Informe a quantidade de dias que terão vendas registradas: "))

# Verificacão

if dias <= 0:
    print('Quantidade de dias inválida. O programa será encerrado.')
else:
    print("Quantidade de dias registrada com sucesso!")

print("Você poderá informar os valores de venda de cada dia posteriormente.")

# Variáveis

total_vendido = 0
dias_sem_venda = 0
contador = 1
maior_venda = 0
menor_venda = 0

# Loop

while contador <= dias:
    valor = float(input("Dia " + str(contador) + ": R$ "))
    if valor < 0:
        valor = 0
    total_vendido += valor
    if valor == 0:
        dias_sem_venda += 1

    # Maior venda

    if valor > maior_venda:
        maior_venda = valor

    # Menor venda

    if contador == 1:
        menor_venda = valor
    else:
        if valor < menor_venda:
            menor_venda = valor
            
    contador += 1

# Cálculo da média

if dias > 0:
    media_vendas = total_vendido / dias
else:
    media_vendas = 0

# Meta

meta_mensal = 10000 # 100%

# Percentual

percentual_meta = (total_vendido / meta_mensal) * 100

# Classificando a eficiência de meta mensal

if total_vendido < meta_mensal * (85 / 100):
    classificacao = 'Aproveitamento Regular'
elif total_vendido <= meta_mensal:
    classificacao = 'Aproveitamento Bom'
elif total_vendido < meta_mensal * (125 / 100):
    classificacao = 'Aproveitamento Ótimo'
else:
    classificacao = 'Aproveitamento Excelente'

# Resultados
print('\n************ RESULTADOS **************')
print(f'Total vendido: R$ {total_vendido:.2f}')
print(f'Média diária: R$ {media_vendas:.2f}')
print(f'Maior venda: R$ {maior_venda:.2f}')
print(f'Menor venda: R$ {menor_venda:.2f}')
print(f'Dias sem venda: {dias_sem_venda}')
print(f'Percentual da meta: {percentual_meta:.2f}%')
print(f'Classificação: {classificacao}')