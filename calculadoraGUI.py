import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QLabel,QWidget,QGridLayout
from PyQt5.QtWidgets import QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,400,500) # dimensões da calculadora

		self.calculo = QLabel("",self) # variáveis de cálculo
		self.conta=""

		self.botão1 = QPushButton("1",self) #declaração de todos os botões
		self.botão2 = QPushButton("2",self)
		self.botão3 = QPushButton("3",self)
		self.botão4 = QPushButton("4",self)
		self.botão5 = QPushButton("5",self)
		self.botão6 = QPushButton("6",self)
		self.botão7 = QPushButton("7",self)
		self.botão8 = QPushButton("8",self)
		self.botão9 = QPushButton("9",self)
		self.botão0 = QPushButton("0",self)
		self.botão_mais = QPushButton("+",self)
		self.botão_menos = QPushButton("-",self)
		self.botão_vezes = QPushButton("*",self)
		self.botão_div = QPushButton("/",self)
		self.botão_igual = QPushButton("=",self)
		self.botão_ponto = QPushButton(".",self)
		self.botão_apaga = QPushButton("CE",self)
		self.initUI()
		
	def initUI(self):

		CW = QWidget()
		self.setCentralWidget(CW)

		self.calculo.setGeometry(10,10,400,30)
		self.calculo.setStyleSheet("font-size: 25px; font-family: Comic Sans MS")

		grid=QGridLayout()  #grid
	
		grid.addWidget(self.botão1,1,0)	#posicionamento de cada botão na grid
		grid.addWidget(self.botão2,1,1)
		grid.addWidget(self.botão3,1,2)
		grid.addWidget(self.botão_apaga,5,0)
		grid.addWidget(self.botão4,2,0)
		grid.addWidget(self.botão5,2,1)
		grid.addWidget(self.botão6,2,2)
		grid.addWidget(self.botão_mais,1,3)
		grid.addWidget(self.botão7,3,0)
		grid.addWidget(self.botão8,3,1)
		grid.addWidget(self.botão9,3,2)
		grid.addWidget(self.botão_menos,2,3)
		grid.addWidget(self.botão0,4,1)
		grid.addWidget(self.botão_ponto,4,0)
		grid.addWidget(self.botão_igual,4,2)
		grid.addWidget(self.botão_vezes,3,3)
		grid.addWidget(self.botão_div,4,3)
		grid.addWidget(self.botão1,1,3)

		self.botão1.clicked.connect(self.clique1)	#interação de clique nos botões com as funções
		self.botão2.clicked.connect(self.clique2)
		self.botão3.clicked.connect(self.clique3)
		self.botão4.clicked.connect(self.clique4)
		self.botão5.clicked.connect(self.clique5)
		self.botão6.clicked.connect(self.clique6)
		self.botão7.clicked.connect(self.clique7)
		self.botão8.clicked.connect(self.clique8)
		self.botão9.clicked.connect(self.clique9)
		self.botão0.clicked.connect(self.clique0)
		self.botão_mais.clicked.connect(self.clique_mais)
		self.botão_menos.clicked.connect(self.clique_menos)
		self.botão_vezes.clicked.connect(self.clique_vezes)
		self.botão_div.clicked.connect(self.clique_div)
		self.botão_ponto.clicked.connect(self.clique_ponto)
		self.botão_apaga.clicked.connect(self.clique_apaga)
		self.botão_igual.clicked.connect(self.clique_igual)

		
		CW.setLayout(grid)	#mostra a grid
	
	# Cada função de cada função. Todas elas adicionam o que está escrito no botão (com exceção do igual e CE) à variável conta, que é mostrada no label de calculo

	def clique1(self,estado):
		if estado==False:
			self.conta+="1"
			self.calculo.setText(f"{self.conta}")
	
	def clique2(self,estado):
		if estado==False:
			self.conta+="2"
			self.calculo.setText(f"{self.conta}")
	
	def clique3(self,estado):
		if estado==False:
			self.conta+="3"
			self.calculo.setText(f"{self.conta}")
	
	def clique4(self,estado):
		if estado==False:
			self.conta+="4"
			self.calculo.setText(f"{self.conta}")

	def clique5(self,estado):
		if estado==False:
			self.conta+="5"
			self.calculo.setText(f"{self.conta}")

	def clique6(self,estado):
		if estado==False:
			self.conta+="6"
			self.calculo.setText(f"{self.conta}")
	
	def clique7(self,estado):
		if estado==False:
			self.conta+="7"
			self.calculo.setText(f"{self.conta}")

	def clique8(self,estado):
		if estado==False:
			self.conta+="8"
			self.calculo.setText(f"{self.conta}")

	def clique9(self,estado):
		if estado==False:
			self.conta+="9"
			self.calculo.setText(f"{self.conta}")

	def clique0(self,estado):
		if estado==False:
			self.conta+="0"
			self.calculo.setText(f"{self.conta}")

	def clique_mais(self,estado):
		if estado==False:
			self.conta+="+"
			self.calculo.setText(f"{self.conta}")

	def clique_menos(self,estado):
		if estado==False:
			self.conta+="-"
			self.calculo.setText(f"{self.conta}")
	
	def clique_vezes(self,estado):
		if estado==False:
			self.conta+="*"
			self.calculo.setText(f"{self.conta}")

	def clique_div(self,estado):
		if estado==False:
			self.conta+="/"
			self.calculo.setText(f"{self.conta}")

	def clique_ponto(self,estado):
		if estado==False:
			self.conta+="."
			self.calculo.setText(f"{self.conta}")

	def clique_apaga(self,estado):
		if estado==False:
			self.conta=""							# Adiciona vazio, ou seja, apaga o texto
			self.calculo.setText(f"{self.conta}")

	def clique_igual(self,estado):
		if estado==False:						# estado == False significa que o botão foi clicado
			try:
				self.conta = eval(self.conta)	#Função eval dentro de um try block para evadir erros
				self.conta = str(self.conta)	#transforma em string novamente para não dar erros
				self.calculo.setText(f"{self.conta}")
			except Exception:					#caso um erro de conta ou sintaxe ocorra, aparecerá error no display
				self.calculo.setText(f"ERROR!")
		
def main():										#cria a janela
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()