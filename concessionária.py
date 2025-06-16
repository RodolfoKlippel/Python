import os
import csv

Local_Arquivo = "C:/Users/RODOLFO/Desktop/arquivo.csv"
lista = [{'nome': 'MUSTANG', 'preco': '10000', 'estoque': '1', 'ano': '2020'},{'nome': 'FERRARI', 'preco': '15000', 'estoque': '1', 'ano': '2000'},{'nome': 'LAMBORGHINI', 'preco': '14000', 'estoque': '1', 'ano': '1990'}, {'nome': 'LIMOUSINE', 'preco': '40000', 'estoque': '1', 'ano': '1970'}]
caixa = 15000

def existe_arquivo():
	if os.path.exists(Local_Arquivo):
		dados = analise()
		Arquivo(dados)
	else:
		Arquivo(lista)

def Arquivo(dados):
	with open(Local_Arquivo,"w",newline="") as arq:
		cabecalho = ["nome","preco","estoque","ano"]
		escreve = csv.DictWriter(arq,fieldnames=cabecalho,delimiter=";")

		escreve.writeheader()
		for linha in dados[0:]:
			escreve.writerow(linha)

def analise():
	dados = []
	with open(Local_Arquivo,"r",encoding="utf8") as arq:

		checa = csv.DictReader(arq, delimiter=";")
		for linha in checa:
			dados.append(linha)
	return dados

def venda():
	global caixa
	dados = analise()
	carro_venda = input("Diga o carro que deseja vender: ").upper()
	preco_venda = int(input("Diga o valor pelo qual deseja vender: "))
	ano_carro = int(input("Diga o ano do carro: "))

	decisao = input("O dono aceita comprar? [S/N] ").upper()
	if decisao == "S":
		print("\nCompra Realizada.\n")
		for i in range(len(dados)):
			if carro_venda == dados[i]['nome']:
				caixa-=preco_venda
				dados[i]['estoque'] = int(dados[i]['estoque']) + 1
				break

			elif carro_venda not in dados[i].values() and i==len(dados)-1:
				caixa-=preco_venda
				carro = {
					"nome":carro_venda,
					"preco":str(preco_venda*1.2),
					"estoque":"1",
					"ano":str(ano_carro)
				}
				dados.append(carro)
		Arquivo(dados)
	elif decisao == "N":
		print("\nCompra não realizada.\n")
	else:
		print("\nValor Inválido.\n")

def compra():
	global caixa
	dados = analise()
	carro_venda = input("Diga o carro que deseja comprar: ").upper()

	for i in range(len(dados)):
		if carro_venda == dados[i]['nome']:
			decisao = input(f"\nO carro custará {int(dados[i]['preco']) * 1.31}\nVocê aceita? [S/N] ").upper()
			if decisao == "S":
				print("\nCompra Realizada.\n")
				caixa+=int(dados[i]['preco'])*1.3
				dados[i]['estoque'] = int(dados[i]['estoque']) - 1

				if dados[i]['estoque'] == 0:
					dados.pop(i)
				Arquivo(dados)
			elif decisao == "N":
				print("\nCompra não realizada.\n")
			else:
				print("\nValor Inválido.\n")
			break
		elif carro_venda != dados[i]['nome'] and i == len(dados) - 1:
			print("\nCarro não encontrado.\n")

if __name__ == "__main__":
	existe_arquivo()
	while True:
		print(f"\n{caixa}\n")
		menu=input("""\nDiga o que você deseja fazer:\n\n(C) Comprar um Carro\n(V) Vender um Carro\n(S) Para Sair\n""").upper()
		
		os.system("cls")
		match(menu):
			case "S":
				existe_arquivo()
				break
			case "C":
				compra()
			case "V":
				venda()
			case _:
				print("\nOpção Inválida.")
