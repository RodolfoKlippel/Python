import time
import math
import random

ale = random.randint(0, 2)

jogadas = ["pedra","papel","tesoura"]
jogador = ""
computador = jogadas[ale]

while jogador not in jogadas:
    jogador=input("Diga a sua jogada: ").lower()

print(F"\njogada do jogador: {jogador}\nJogada do computador: {computador}\n")

if computador==jogador:
    print("Empate.")
elif jogador == "pedra" and computador == "tesoura":
    print("Vitória dos Humanos.")
elif jogador == "papel" and computador == "pedra":
    print("Vitória dos Humanos.")
elif jogador == "tesoura" and computador == "papel":
    print("Vitória dos Humanos.")
else:
    print("Vitória das Máquinas")