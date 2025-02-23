import os

print(os.getcwd()) # Mostra o diretório atual
print(os.listdir()) # Mostra os arquivos do diretório atual

#exercicio passar todos txt para as pastas
lista_diretorios = os.listdir()
print(lista_diretorios)
path = os.getcwd()

# for nome_do_arquivo in lista_diretorios:
#     if "txt" in nome_do_arquivo:
#         if "22" in nome_do_arquivo:
#             os.rename(f"{path}/{nome_do_arquivo}", f"{path}/22/{nome_do_arquivo}")
#         elif "23" in nome_do_arquivo:
#             os.rename(f"{path}/{nome_do_arquivo}", f"{path}/23/{nome_do_arquivo}")


# diretorio = "22"
# for nome_do_dir in lista_diretorios:
#      if nome_do_dir == diretorio:
#          for nome_arquivo in os.listdir(f"{nome_do_dir}"):
#             nome_arquivo_novo = nome_arquivo[:nome_arquivo.find(".")]
             
#             os.rename(f"{os.getcwd()}/{diretorio}/{nome_arquivo}", f"{os.getcwd()}/{diretorio}/{nome_arquivo_novo.capitalize()}.txt")


# import requests 

# CEP = "09134230"
# link = f"https://viacep.com.br/ws/{CEP}/json/"
# cep = requests.get(link) 

# print(cep.json())