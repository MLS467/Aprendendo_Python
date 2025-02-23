dic_lista_produtos = {"iphone": 5000, "galaxy": 3000, "nokia": 1000}

# pegar o valor de um produto
print(dic_lista_produtos["iphone"])
# ou
print(dic_lista_produtos.get("iphone"))

dic_de_funcionarios = {"joao": [2000,500,800], "maria": [3000,200], "pedro": 4000} #dicionario com listas dentro dele

#editar e adicionar um valor

dic_lista_produtos["galaxy"] *= 1.1 #aumento de 10% no valor do galaxy 

dic_lista_produtos["Tijolao"] = 9000; #adicionando um novo produto

print(dic_lista_produtos)

#Excluir um valor

dic_lista_produtos.pop("nokia") #excluindo o nokia
print(dic_lista_produtos)

#verificar se um valor existe no dicionario

print("Tijolao" in dic_lista_produtos) #retorna False dic_lista_produtos.keys()

print(2000 in dic_lista_produtos.values()) #retorna True


print(list(dic_lista_produtos.keys())) #retorna uma lista com as chaves do dicionario
print(list(dic_lista_produtos.values())) #retorna uma lista com os valores do dicionario


#exercicio

# quero 15 produtos sem repetição
dic_list_produtos = {
    "iphone": 5000,
    "galaxy": 3000,
    "nokia": 1000,
    "tijolao": 9000,
    "samsung": 4000,
    "xiaomi": 2000,
    "motorola": 1500,
    "lg": 1200,
    "sony": 3000,
    "asus": 2500,
    "lenovo": 2000,
    "huawei": 3000,
    "oppo": 2500,
    "vivo": 2000,
    "oneplus": 3000
} 


produto_procurado = input("Digite o nome do produto: ")
produto_procurado = produto_procurado.lower().strip()

if produto_procurado in dic_list_produtos:
    print(f"O valor do produto {produto_procurado} é R${dic_list_produtos[produto_procurado]:.2f}")
else:
    print("Produto não encontrado")