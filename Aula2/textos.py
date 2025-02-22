faturamento = 1000
custo = 500

lucro = faturamento - custo


print(f"O lucro foi {lucro} e o faturamento foi {faturamento}")

email = " EmailFalso@gmail.cOM " # Email falso sem formatação

email = email.lower() # Deixa tudo em minúsculo

print(email)

email = email.strip() # Remove espaços em branco    

print(email)

print(len(email)) # Mostra o tamanho da string

posicao = email.find("@")
print(posicao) # Mostra a posição do @


print(email[:posicao]) # Mostra o que tem depois do @
print(email[posicao: ]) # Mostra o que tem depois do @

novo_email = email.replace("gmail", "hotmail") # Substitui gmail por hotmail
print(novo_email)

nome = "maisson leal"

print(nome.capitalize())    # Deixa a primeira letra maiúscula
print(nome.title())         # Deixa a primeira letra de cada palavra maiúscula
print(nome.upper())         # Deixa tudo maiúscula

print(nome.split())         # Separa as palavras em uma lista

faturamento = 1_000_000
custo = 500.00
marge = lucro/faturamento


print(f"O lucro foi {lucro:,.2f} e o faturamento foi {faturamento:,.1f} e a margem é de {marge:.2%}") # F-String


nome = "joao paulo lira"
email = "emailfalsodolira@gmail.com"

print("EXERCICIO\n")
print(email[email.find("@")+1:])

primeiro_nome = nome.split()[0].title()
print(primeiro_nome)

mensagem_personalizada = f"O Usuario {primeiro_nome} foi cadastrado com sucessso com o email {email}"
print(mensagem_personalizada)


