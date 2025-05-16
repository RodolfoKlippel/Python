import time
import math
import os

palavra=input("Qual será a Palavra da forca? ")

os.system('cls')

letras = [""]*8

LP = len(palavra)

trava = [0]*LP

for i in range (0,8):
    letras[i]=input(f"\nDiga a {i+1}° Letra: ")
    print()
    for z in range(0,8):
        for j in range (0,LP):
            if letras[z]==palavra[j]:
                trava[j]=1
    os.system('cls')
    for h in range(0,LP):
        print(palavra[h] if trava[h] == 1 else"_",end="")

RespFinal=input("\nQual você acha que é a palavra? ")

if RespFinal == palavra:
    print("\nVocê Ganhou!!!")
else:
    print("\nVocê perdeu...")
