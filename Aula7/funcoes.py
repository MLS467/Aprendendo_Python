valores_precos = [10, 20, 30, 40, 50]


def calcular_soma(list):
    return sum(list)

print(calcular_soma(valores_precos))



def retorna_taxa(param):
    if param > 20:
        taxa = param *  0.1
    else:
        taxa =  param * 0.05

    return taxa


def retorna_imposto_total(list):
    lista_impostos = []
    for param in list:

        taxa = retorna_taxa(param)
        
        lista_impostos.append(taxa)
    
    return sum(lista_impostos)


print(retorna_imposto_total(valores_precos))