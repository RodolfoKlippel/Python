import os
import string
import random

def main():
	alpha = list(" "+string.punctuation+string.digits+string.ascii_letters)
	encript = list(" "+string.punctuation+string.digits+string.ascii_letters)
	random.shuffle(encript)
	mensagem=""
	
	while True:
		decisao=input("O que você deseja fazer?\n(N) Para criar um mensagem\n(P) Para printar a mensagem\n(E) Para encriptar esta mensagem\n(D) Para desencriptar essa mensagem\n(S) Para sair\n").upper()
		if decisao=="S":
			break
		os.system("cls")
		if decisao=="N":
			mensagem=novaMensagem(mensagem)
		elif decisao=="E":
			mensagem=encriptar(mensagem,alpha,encript)
		elif decisao=="D":
			mensagem=desencriptar(mensagem,alpha,encript)
		elif decisao=="P":
			print(mensagem)
			print()
		else:
			print("Mensagem inválida")

def novaMensagem(mensagem):
	mensagem=input("Diga uma nova mensagem: ")
	return mensagem
	os.system("cls")

def encriptar(mensagem,alpha,encript):
	texto=""
	for i in range(0,len(mensagem)):	
		if mensagem[i] in alpha:
			texto+=encript[alpha.index(mensagem[i])]
	return texto

def desencriptar(mensagem,alpha,encript):
	texto=""
	for i in range(0,len(mensagem)):	
		if mensagem[i] in encript:
			texto+=alpha[encript.index(mensagem[i])]
	return texto
	
if __name__ == "__main__":
	main()
