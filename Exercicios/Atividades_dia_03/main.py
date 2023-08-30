from funcoes import soma,soma_sem_parametro,print_subtracao
import itertools

x = 10
y = 5.2

print(f"{x=}")
print(f"{y=}")

soma = soma(x,y)
print(soma)

print(soma_sem_parametro())

print(print_subtracao(x,y))

# itertools.cycle()