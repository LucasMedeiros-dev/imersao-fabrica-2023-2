
from os import system
# Verificador de idade cnh
# Recebe um input e verifica se a pessoa te ao menos 18 anos

while True:
    system('cls')
    idade = input("Insira sua idade: ")
    
    try:
        idade = int(idade)
        if idade >= 18:
            print("Apto a receber uma CNH")
            input("Pressione qualquer coisa para prosseguir")
        else:
            print("Para receber uma CNH é necessário ser maior de 18 anos")
            input("Pressione qualquer coisa para prosseguir")
        
    except:
        print("Ops parece que você inseriu algo inválido, tente novamente")
        input("Pressione qualquer coisa para prosseguir")