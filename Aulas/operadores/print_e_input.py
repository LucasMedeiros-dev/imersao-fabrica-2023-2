import random # Importa a biblioteca random do python com sua pseudo-aleatoriedade
import os

valor_random = random.randint(0,10) # Cria uma var com um valor random entre 0 a 10.

print("Está se sentindo com sorte?") # Exibe no terminal
input("Aperte qualquer coisa para prosseguir") # Cria um input que será perdido na memória
os.system('cls')
print(f"Você estava se sentindo com sorte hein... sua nota é: {valor_random}") # Exibe no terminal

if valor_random < 7:
    print("Não se sinta mal... \ntente de novo, mais sorte na próxima.")