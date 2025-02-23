# teste = ['batata', 'arroz', 'feijao']


# novo_produto = input('Digite o nome do produto: ')


# if novo_produto in teste:
#     print('O produto já existe')
# else:
#     teste.append(novo_produto)
#     print('Produto adicionado com sucesso')

# print(teste)

vendas_da_empresa = 99_999
vendas_funcionario = 10_000
meta_da_empresa = 50_000

if vendas_da_empresa >= meta_da_empresa:
    if vendas_funcionario >= 15_000:
        bonus = 500
    elif vendas_funcionario < 15_000 & vendas_funcionario >= 10_000:
        bonus = 300
    else:
        bonus = 100
else:
    bonus = 0

print(f'O valor do bônus é de R${bonus}')