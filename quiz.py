import time
import math
import os


perguntas = ["Qual o maior Estado do Brasil?",
             "Em que ano foi a Ditadura Brasileira?",
             "Qual foi o maior império de terra contínua do mundo?",
             "Qual foi o primeiro presidente do Brasil?",
             "Qual o elemento com a maior massa?"]

perguntas2 = [["A.Minas Gerais","B.São Paulo","C.Bahia","D.Amazônas"],
             ["A.1986","B.1957","C.1964","D.1945"],
             ["A.Reino Unido","B.Império Romano","C.Império Otomano","D.Império Mongol"],
             ["A.Deodoro da Fonseca","B.Castelo Branco","C.Floriano Peixoto","D.Médice"],
             ["A.Ferro","B.Oganessônio","C.Tungstênio","D.Diamante"]]

respostas = ["D",
             "C",
             "D",
             "A",
             "B"]
pontuacao=0

for i in range(0,5):
    print(f"------------{i+1}° PERGUNTA------------")
    print(f"{perguntas[i]}")
    print()
    for j in range(0,4):
        print(f"{perguntas2[i][j]}")
    minhaResp=input("\nQual alternativa você acha que é verdadeira? ").upper()
    if minhaResp==respostas[i]:
        print("Resposta Correta!!!\n")
        pontuacao+=1
    else:
        print(f"Resposta Incorreta...\nA alternativa correta era: {respostas[i]}\n")
print(f"Fim de jogo!\nSua pontuação é: {pontuacao}")