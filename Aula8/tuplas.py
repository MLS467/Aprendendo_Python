lista_vendas_funcionario = [10,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]


def calcula_bonus(list):  # calcula_bonus(lista_vendas_funcionario) 
  valor_vendas = 2 * len(list) 
  valor_bonus_vendas = 0.01 * sum(list)
  return valor_vendas, valor_bonus_vendas

def printa_tupla(lista_tupla): # lista_tupla = [(10,20,30), (40,50,60), (70,80,90)] 
    for val1,val2,val3 in lista_tupla: #unpacking de tupla
        print(val1,val2,val3)

valor_vendas_funcionario, valor_bonus_funcionario = calcula_bonus(lista_vendas_funcionario)
print(f"O valor das vendas do funcionário é R${valor_vendas_funcionario:.2f} e o valor do bônus é R${valor_bonus_funcionario:.2f}")


lista_tupla = [(10,20,30), (40,50,60), (70,80,90)]

printa_tupla(lista_tupla)




#exercicio 

vendas = {
    'João': [100, 200, 400, 500],
    'Pedro': [200, 300, 300, 400],
    'Joaquim': [400, 400, 500, 600],
    'Maria': [200, 300, 300, 400]
}


lista_de_bonus = []
for funcionario in vendas:
   valor1,valor2 = calcula_bonus(vendas[funcionario])
   valor_bonus_total = valor1 + valor2
   lista_de_bonus.append(valor_bonus_total) 
   print(f"O funcionario {funcionario} tem o bonus 1 R${valor1:.2f} e bonus 2 R${valor2:.2f} então o total R${valor_bonus_total:.2f}")

print(f"O total de bonus é R${sum(lista_de_bonus):.2f}")
