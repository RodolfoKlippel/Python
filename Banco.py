import os

# Sistema bancário

def balanca(valor):
	print(f"\nSua balança atualmente é de: R${valor:.2f}\n")	#Mostra a balança

def extrato(valor):
	while True:
		sacar=float(input("Quanto você deseja sacar? "))
		if sacar>valor:			#Não deixa sacar mais do que há na conta
			os.system("cls")
			print("Valor insuficiente na conta.\n")
		elif sacar>=1000:		#Limite da conta
			os.system("cls")
			print("Não é possível realizar transações com valores maiores do que R$1000.00 reais.\n")
		elif sacar>=0:			#Retorna valor sacado
			os.system("cls")
			print("Transação executada.\n") 
			return sacar		#Remove fundos à conta
		else:					#Comando inválido de segunrança
			os.system("cls")
			print("Comando inválido.\n")
	
def inserir(): 
	while True:
		insere=float(input("Quanto você deseja adicionar à sua conta? "))
		if insere>=0:
			os.system("cls")
			print("Transação executada.\n")
			return insere	#Adiciona fundos à conta
		else:
			os.system("cls")
			print("Comando inválido.\n")	#Se valor for negativo, comando inválido

def main():
	conta=1000.00
	while True:
		decisao=input("O que você deseja fazer?\n(B) Para ver balança\n(E) Para sacar\n(I) Para inserir dinherio\n(S) Para sair\n").upper()
		if decisao=="S":
			break
		os.system("cls")
		if decisao=="B":
			balanca(conta)
		elif decisao=="E":
			conta-=extrato(conta)		#Valor retornado é subtraído
		elif decisao=="I":
			conta+=inserir()			#Valor retornado é somado
		else:
			print("Comando inválido.")
	
if __name__ == "__main__":
	main()						
