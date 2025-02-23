lista_de_valores = [100,521,36,99,5,8,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]

print(sum(lista_de_valores)) # Soma todos os valores da lista

print(lista_de_valores[-1]) # Retorna o último valor da lista

print(max(lista_de_valores)) # Retorna o maior valor da lista
print(min(lista_de_valores)) # Retorna o menor valor da lista
print(str(round((sum(lista_de_valores)/len(lista_de_valores)),2)).replace(".",",")) # Retorna a média dos valores da lista


lista_compras = [
    "batata",      # Lista de compras
    "arroz",
    "feijão",
    "macarrão",
    "carne",
    "frango",
    "peixe",
    "leite",
]


print(lista_compras.index("carne")) # Retorna o índice do valor "carne" na lista
print(lista_compras[:lista_compras.index("carne")+1]) # Retorna os valores da lista até o valor "carne"


lista_de_precos = [10,20,30,40,50,60,70,80,90,100]

posicao = lista_de_precos.index(80);


lista_de_precos[posicao] *= 1.2 # Aumenta o valor do primeiro item da lista em 20%

print(lista_de_precos) # Exibe a lista de preços



# lista_de_precos.remove(100) # Remove o valor 100 da lista
item_removido = lista_de_precos.pop(-1)
print(item_removido) # Exibe a lista de preços

print(lista_de_precos) # Exibe a lista de preços


lista_de_precos.append(150) # Adiciona o valor 150 ao final da lista
print(lista_de_precos) # Exibe a lista de preços


nova_lista_de_precos = [110,120,130,140,150]

lista_de_precos.extend(nova_lista_de_precos) # Adiciona os valores da nova lista ao final da lista original
print(lista_de_precos) # Exibe a lista de preços


lista_de_precos.insert(5,666) # Adiciona o valor 666 na posição 5 da lista

print(lista_de_precos) # Exibe a lista de preços

lista_de_precos.append(666) # Adiciona o valor 666 ao final da lista

qtde = lista_de_precos.count(666) # Conta quantas vezes o valor 666 aparece na lista
print(qtde) # Exibe a quantidade de vezes que o valor 666 aparece na lista


lista_de_precos.sort() # Ordena a lista em ordem crescente
print(lista_de_precos) # Exibe a lista de preços

lista_de_precos.sort(reverse=True) # Ordena a lista em ordem decrescente
print(lista_de_precos) # Exibe a lista de preços

