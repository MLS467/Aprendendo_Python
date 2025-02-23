# Aula sobre laço de repetição for
# for i in range(10):
#     print(i+1)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# taxa = 0.1

# for elemento in lista:
#     print(f"elemento é {elemento}")
#     print(f"elemento ao taxa de 10% é {elemento*taxa}")

# cont = 0
# while cont < 10:
#     print(lista[cont])
#     cont += 1


preco_produtos = [80,251, 100, 150, 200, 300, 400, 500, 600,1004,1500]


# for preco in preco_produtos:
#     if preco > 1000:
#         print(f"Produto taxa 15% : {preco + (preco * 0.15):.2f}")
#     else:
#         print(f"Produto barato 10% : {preco + (preco * 0.10):.2f}")


acum = []
for preco in preco_produtos:
    if preco > 1000:
        taxa = 0.15
        print(f"Produto taxa 15% : {preco + (preco * 0.15):.2f}")
    else:
        taxa = 0.10
        print(f"Produto barato 10% : {preco + (preco * 0.10):.2f}")
    
    acum.append(preco * taxa)

print(acum)
print(f"Total de taxa: {sum(acum):.2f}")