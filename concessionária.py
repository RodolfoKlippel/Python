import random
import time
import os

Local_Arquivo = "C:/Users/RODOLFO/Desktop/arquivo.json"
lista=[["MUSTANG","FERRARI","LAMBORGHINI","BULGATI","LIMOUSINE"],
        [10000,15000,14000,20000,40000],
        [1,1,1,1,1]]
caixa=[15000]

def menuCarros():
    aux=1
    for i in range(0,len(lista[0])):
        if lista[2][i]>0:
            print(aux,". ",lista[0][i])
            aux+=1

def Arquivo():
	with open(Local_Arquivo,"w") as arq:
		arq.write("Planilha da Empresa:\n")
		for j in range(0,len(lista[0])):
			arq.write(f"O carro {lista[0][j]} Possui o preço de {lista[1][j]} e Um estoque de {lista[2][j]} carro\n")
		arq.write(f"O caixa é de: {caixa[0]}")

def venda():
	carroDeVenda=input("Diga o carro que você deseja vender: ").upper()
	precoCarro=int(input("Diga o preço que você quer pelo carro: "))
	for i in range(len(lista[0])):
		if (caixa[0]-precoCarro)<0:
			os.system("cls")
			print("Compra impossível.")
			break
		if carroDeVenda == lista[0][i]:
			if precoCarro < lista[1][i]*0.84:
				print("\nO carro foi vendido!")
				caixa[0]=caixa[0]-precoCarro
				lista[2][i]+=1
				break
			else:
				respDono=input("\nO dono da concessionária irá aceitar a oferta? ").upper()
				if respDono=="S":
					print("\nO carro foi vendido!")
					caixa[0]=caixa[0]-precoCarro
					lista[2][i]+=1
					break
				elif respDono=="N":
					print("\nO carro não foi vendido.")
					break
				elif respDono not in ["S","N"]:
					print("\nResposta inválida\n")
					break
		elif carroDeVenda != lista[0][i] and i==len(lista[0])-1:
			respDono=input("\nO dono da concessionária irá aceitar a oferta? ").upper()
			if respDono=="S" and (caixa[0]-precoCarro)>=0:
				print("\nO carro foi vendido!")
				caixa[0]=caixa[0]-precoCarro
				lista[0].append(carroDeVenda)
				lista[1].append(precoCarro)
				lista[2].append(1)
				break
			elif respDono=="N":
				print("\nO carro não foi vendido.")
				break
			elif respDono not in ["S","N"]:
				print("\nResposta inválida\n")
				break

def aluguel():
	aluguel=85
	print("Lista de carros abertos para Aluguel:\n")
	menuCarros()
	carroAlugado=input("Diga o carro que deseja alugar: ").upper()
	for i in range(len(lista[0])):
		if carroAlugado == lista[0][i]:
			dias=int(input("Por quantos dias você deseja alugá-lo? "))
			respAlug=input(f"\nO preço do aluguel do {lista[0][i]} será: R${aluguel*dias:.2f}\nVocê aceita a oferta? [S/N] ").upper()
			os.system("cls")
			if respAlug=="S":
				print("\nO carro foi alugado!")
				caixa[0]=caixa[0]+aluguel*dias
				break
			elif respAlug=="N":
				print("\nO carro não foi alugado.")
				break
			else:
				print("\nResposta inválida\n")
				break
		elif carroAlugado != lista[0][i] and i == len(lista[0])-1:
			print("Carro não encontrado.")
	
	
def compra():
	
	print("\nLista de carros Que podem ser comprados:")
	menuCarros()
	carroComprado=input("\nDiga o carro que deja comprar: ").upper()

	if carroComprado not in lista[0]:
		os.system("cls")
		print("Opção inválida.")

	for i in range(len(lista[0])):
		if carroComprado == lista[0][i]:
			preco=lista[1][i]*1.31
			decisao=input(f"O preço do carro será: R${preco:.2f}\nVocê aceita? [S/N] ").upper()
			os.system("cls")
			if decisao=="S":
				print("Compra realizada!")
				caixa[0]=caixa[0]+preco
				lista[2][i]-=1
				if lista[2][i]==0:
					lista[0].remove(lista[0][i])
					lista[1].remove(lista[1][i])
					lista[2].remove(lista[2][i])
				break
			elif decisao=="N":
				print("Compra não realizada.")
				break
			elif decisao not in ["S","N"]:
				print("\nResposta inválida\n")
				break
if __name__ == "__main__":
	while True:
		menu=input("\nDiga o que você deseja fazer:\n\n(C) Comprar um Carro\n(V) Vender um Carro\n(A) Alugar um Carro\n(M) Ver Menu\n").upper()
		if menu=="":
			Arquivo()
			break
		os.system("cls")
		if menu=="C":
			compra()
		elif menu=="V":
			venda()
		elif menu=="A":
			aluguel()
		elif menu=="M":
			Arquivo()
		else:
			print("\nOpção Inválida.")
