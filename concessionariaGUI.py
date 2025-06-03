import sys
import datetime
import random
import time
from datetime import datetime
from datetime import timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton,QGridLayout,QWidget,QVBoxLayout

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,300,150)
		self.Texto = QLabel("O que você deseja fazer?",self)
		self.botao1 = QPushButton("COMPRA",self)
		self.botao2 = QPushButton("VENDA",self)
		self.botao3 = QPushButton("ALUGUEL",self)
		self.botao5 = QPushButton("PLANILHA",self)
		self.botao4 = QPushButton("SAIR",self)
		self.botao6 = QPushButton("VOLTAR",self)
		self.line_edit = QLineEdit(self)
		self.botaoLE = QPushButton("SUBMIT",self)
		self.comp = QLabel("Que carro você gostaria de comprar?",self)
		self.vend = QLabel("Qual o nome do carro que você deseja vender?",self)
		self.planilha_direta = QLabel("",self)
		self.botao_sim = QPushButton("SIM",self)
		self.botao_nao = QPushButton("NÃO",self)

		self.line_edit.hide()
		self.botaoLE.hide()
		self.comp.hide()
		self.vend.hide()
		self.planilha_direta.hide()
		self.botao6.hide()
		self.botao_sim.hide()
		self.botao_nao.hide()

		self.lista=[["MUSTANG","FERRARI","LAMBORGHINI","BULGATI","LIMOUSINE"],
        [10000,15000,14000,20000,40000],
        [1,1,1,1,1]]
		self.caixa=15000
		
		# self.botao_sim.clicked.connect(self.carro_comprado)

		self.initUI()

	def initUI(self):
		self.vbox = QVBoxLayout()

		self.vbox.addWidget(self.Texto)
		self.vbox.addWidget(self.botao1)
		self.vbox.addWidget(self.botao2)
		self.vbox.addWidget(self.botao3)
		self.vbox.addWidget(self.botao5)
		self.vbox.addWidget(self.botao4)
		self.vbox.addWidget(self.vend)
		self.vbox.addWidget(self.comp)
		self.vbox.addWidget(self.line_edit)
		self.vbox.addWidget(self.botaoLE)
		self.vbox.addWidget(self.planilha_direta)
		self.vbox.addWidget(self.botao6)
		self.vbox.addWidget(self.botao_sim)
		self.vbox.addWidget(self.botao_nao)
		
		self.setLayout(self.vbox)

		self.Texto.setAlignment(Qt.AlignCenter)
		
		self.setStyleSheet("""
					QPushButton{ font-size:15px;
					font-family:Comic Sans MS;
					}
					QLabel{font-size:15px; 
					font-family:Comic Sans MS;
					}
					QLineEdit{font-size:15px; 
					font-family:Comic Sans MS;
					}
				""")
		self.botao1.clicked.connect(self.compra)
		self.botao2.clicked.connect(self.venda)
		self.botao3.clicked.connect(self.aluguel)
		self.botao5.clicked.connect(self.planilha)
	
	def compra(self):
		self.some()

		self.comp.show()
		self.line_edit.show()
		self.botaoLE.show()

		self.setLayout(self.vbox)

		self.comp.setAlignment(Qt.AlignCenter)

		self.botaoLE.clicked.connect(self.compra_decisao)
		
	def compra_decisao(self):
		self.carroComp = self.line_edit.text().upper()
		for i in range(0,len(self.lista[0])):
			if self.carroComp == self.lista[0][i]:
				self.comp.setText(f"O carro irá custar: {self.lista[1][i]*1.31}\nVocê aceita?")
				break
		self.line_edit.hide()
		self.botaoLE.hide()
		self.botao_sim.show()
		self.botao_nao.show()
		
		self.botao_nao.clicked.connect(self.aparece)
		
		try:
			self.botao_sim.clicked.disconnect()
		except TypeError:
			pass
		
		self.botao_sim.clicked.connect(self.carro_comprado)
		
	def carro_comprado(self):
		self.caixa+=self.lista[1][self.lista[0].index(self.carroComp)]*1.31
		self.lista[2][self.lista[0].index(self.carroComp)]-=1
		if self.lista[2][self.lista[0].index(self.carroComp)] == 0:
			self.lista[2].remove(self.lista[2][self.lista[0].index(self.carroComp)])
			self.lista[1].remove(self.lista[1][self.lista[0].index(self.carroComp)])
			self.lista[0].remove(self.lista[0][self.lista[0].index(self.carroComp)])
		self.aparece()
		self.comp.setText("Que carro você gostaria de comprar?")
        
	def venda(self):
		self.some()

		self.vend.show()
		self.line_edit.show()
		self.botaoLE.show()

		self.setLayout(self.vbox)

		self.vend.setAlignment(Qt.AlignCenter)

		self.botaoLE.clicked.connect(self.aparece)

	def aluguel(self):
		pass

	def planilha(self):
		self.some()
		self.planilha_direta.show()
		self.botao6.show()
		
		self.texto_planilha = ""
		self.texto_planilha += "Planilha da Empresa:\n"
		for j in range(0,len(self.lista[0])):
			self.texto_planilha += f"O carro {self.lista[0][j]} Possui o preço de {self.lista[1][j]} e Um estoque de {self.lista[2][j]} carro\n"
		self.texto_planilha += f"Caixa da Empresa: {self.caixa}"
		
		self.planilha_direta.setText(f"{self.texto_planilha}")
		
		self.botao6.clicked.connect(self.aparece)
		
	def some(self):
		self.Texto.hide()
		self.botao1.hide()
		self.botao2.hide()
		self.botao3.hide()
		self.botao4.hide()
		self.botao5.hide()
	
	def aparece(self):
		self.vend.hide()
		self.comp.hide()
		self.line_edit.hide()
		self.botaoLE.hide()
		self.planilha_direta.hide()
		self.botao6.hide()
		self.botao_nao.hide()
		self.botao_sim.hide()
	
		self.Texto.show()
		self.botao1.show()
		self.botao2.show()
		self.botao3.show()
		self.botao4.show()
		self.botao5.show()
		
def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()
