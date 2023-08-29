# Crie um programa que leia a velocidade de um carro e multe se ele passar de uma velocidade
# Maior que 80 e mostre o valor da multa. O valor da multa é 7 R$ para cada km acima do limite
from os import system

VELOCIDADE_LIMITE = 80

while True:
    system("cls") # Comando para limpar o terminal.
    velocidade = input('Insira a velocidade em km/h (Apenas números): ') # Recebe a velocidade do usuário
    
    try: 
        velocidade = int(velocidade) #
        if velocidade > 80:
            valor_multa = (velocidade - VELOCIDADE_LIMITE) * 7
            excedente = velocidade - VELOCIDADE_LIMITE
            print(
                f"Você passou o radar acima de {VELOCIDADE_LIMITE}\n"
                f"Você excedeu o limite por {excedente} KM/H\n"
                f"Sua multa será {valor_multa} R$\n"
                )
            input("Pressione qualquer coisa para continuar.")
        else:
            print("Velocidade até 80 KM/H, não será multado")
            input("Pressione qualquer coisa para continuar.")
    except:
        print("Ops... parece que a velocidade que você inseriu é inválida")
        input("Pressione qualquer coisa para continuar.")