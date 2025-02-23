faturamento = input("Digite o faturamento da empresa: ")
faturamento = faturamento.replace(",", ".").replace("R$", "").replace(" ", "")

faturamento = float(faturamento)

custo = 600

print(faturamento - custo)
