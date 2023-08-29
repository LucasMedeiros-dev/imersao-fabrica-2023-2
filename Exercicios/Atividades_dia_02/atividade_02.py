
# Atividade sobre operadores

from os import system

while True:
    numero = input("Insira um número qualquer: ")

    try:
        system("cls")
        numero = int(numero)
        antecessor = numero - 1
        sucessor = numero + 1
        print(
            f"Seu número foi: {numero}\n"
            f"Seu antecessor é: {antecessor}\n"
            f"Seu sucessor é: {sucessor}"
            )
    except ValueError:
        system("cls")
        print("Ops... você digitou algo inválido. Tente novamente.")