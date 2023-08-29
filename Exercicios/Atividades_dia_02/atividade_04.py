# Crie um programa que leia a velocidade de um carro e multe se ele passar de uma velocidade
# Maior que 80 e mostre o valor da multa. O valor da multa é 7 R$ para cada km acima do limite
from os import system

VELOCIDADE_LIMITE = 80 # Define a velocidade limite numa constante

while True: # Mantém o código num eterno loop até o usuário quebrá-lo
    system("cls") # Comando para limpar o terminal.
    velocidade = input('Insira a velocidade em km/h (Apenas números): ') # Recebe a velocidade do usuário
    
    try: 
        velocidade = int(velocidade) # Tenta converter a velocidade para inteiro
        if velocidade > 80: # Se a velocidade for maior que 80
            excedente = velocidade - VELOCIDADE_LIMITE # Faz a subtração e multiplica pelo vlaor da multa
            valor_multa = excedente * 7 # DONT REPEAT YOURSELF - obtém o valor da multa multiplicando o excedente e o valor da multa
            
            print(
                f"Você passou o radar acima de {VELOCIDADE_LIMITE}\n"
                f"Você excedeu o limite por {excedente} KM/H\n"
                f"Sua multa será {valor_multa} R$\n"
                )
            input("Pressione qualquer coisa para continuar.") # Espera um input para continuar
        elif velocidade == 80: # Se a velocidade for exatamente 80
            print("Você passou a exatamente 80 KM/H, Atenção.")
            input("Pressione qualquer coisa para continuar.") # Espera um input para continuar
        else:
            print("Velocidade até 80 KM/H, não será multado") # Espera um input para continuar
            input("Pressione qualquer coisa para continuar.") # Espera um input para continuar
    except:
        print("Ops... parece que a velocidade que você inseriu é inválida")
        input("Pressione qualquer coisa para continuar.") # Espera um input para continuar