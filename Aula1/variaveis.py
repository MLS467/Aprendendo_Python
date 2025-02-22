faturamento = 1000
custo = 600

novo_faturamento = 1500

faturamento += novo_faturamento

imposto = 0.20 * faturamento

lucro = faturamento - custo -imposto

print("Faturamento", faturamento)

print("Custo", custo)

print("Imposto", imposto)

print("Lucro", lucro)

mensagem = "O lucro foi de R$"

print(mensagem, lucro)


margem = lucro / faturamento

print("Margem de lucro", margem,"%")

teste = False


print(11//3)

if(teste):{
    print("Teste é verdadeiro")
}
else:
    print("Teste é falso")