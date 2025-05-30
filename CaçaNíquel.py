import sys
import datetime
import random
import time
from datetime import datetime
from datetime import timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton,QGridLayout,QWidget

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,400,200)
		self.timer = QTimer(self)
		self.label = QLabel("",self)
		self.carteira = 100.0
		self.label_carteira = QLabel(f"Sua carteira é: {self.carteira}",self)
		self.simbolos = ["❤️","⭐","🍋","🍒","🔔","💎"]
		self.trava = 0

		self.botão1 = QPushButton("",self)
		self.botão2 = QPushButton("Apostar 1",self)
		self.botão3 = QPushButton("Apostar 5",self)
		self.botão4 = QPushButton("Apostar 25",self)
		self.botão5 = QPushButton("",self)
		self.botão6 = QPushButton("",self)
		self.initUI()

	def initUI(self):
		CW = QWidget()
		self.setCentralWidget(CW)

		grid = QGridLayout()

		grid.addWidget(self.botão1,0,0,1,4)
		self.botão1.setDisabled(True)
		grid.addWidget(self.botão2,1,0)
		grid.addWidget(self.botão3,1,1)
		grid.addWidget(self.botão4,1,2)
		grid.addWidget(self.botão6,2,1)
		self.botão6.setDisabled(True)
		grid.addWidget(self.botão5,3,0,1,4)
		self.botão5.setDisabled(True)

		self.setStyleSheet("""QPushButton{font-size: 25px;
					font-family: Comic Sans Ms;
					padding: 20px;
					margin: 5px;
					border: 2px solid;}

					QPushButton:hover{
						background-color: #999e9b;
					}
					""")

		self.label.setGeometry(118,10,530,80)
		self.label.setStyleSheet("font-size:60px; font-family: Comic Sans MS;")
		
		self.label_carteira.setGeometry(78,295,530,80)
		self.label_carteira.setStyleSheet("font-size:40px; font-family: Comic Sans MS;")

		CW.setLayout(grid)

		self.botão2.clicked.connect(self.roletar1)
		self.botão3.clicked.connect(self.roletar2)
		self.botão4.clicked.connect(self.roletar3)

		# self.timer.timeout.connect(self.continuar)
		# self.timer.start(1000)
	
	def roletar1(self):
		self.simb1 = random.choice(self.simbolos)
		self.simb2 = random.choice(self.simbolos)
		self.simb3 = random.choice(self.simbolos)

		if self.carteira<=0:
			self.label_carteira.setText(f"Dinheiro insuficiente.")
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "❤️":
			self.carteira+=1
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🔔":
			self.carteira+=2
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍋":
			self.carteira+=3
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍒":
			self.carteira+=5
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "⭐":
			self.carteira+=10
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "💎":
			self.carteira+=15
		else:
			self.carteira-=1

		if self.carteira>=0 and self.trava==0:
			if self.carteira == 0:
				self.trava = 1
			self.label.setText(f"{self.simb1}  {self.simb2}  {self.simb3}")
			self.label_carteira.setText(f"Sua carteira é: {self.carteira}")
	
	def roletar2(self):
		self.simb1 = random.choice(self.simbolos)
		self.simb2 = random.choice(self.simbolos)
		self.simb3 = random.choice(self.simbolos)

		if self.carteira<=0:
			self.label_carteira.setText(f"Dinheiro insuficiente.")
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "❤️":
			self.carteira+=5
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🔔":
			self.carteira+=10
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍋":
			self.carteira+=20
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍒":
			self.carteira+=50
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "⭐":
			self.carteira+=100
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "💎":
			self.carteira+=150
		else:
			self.carteira-=5

		if self.carteira>=0 and self.trava==0:
			if self.carteira == 0:
				self.trava = 1
			self.label.setText(f"{self.simb1}  {self.simb2}  {self.simb3}")
			self.label_carteira.setText(f"Sua carteira é: {self.carteira}")
	
	def roletar3(self):
		self.simb1 = random.choice(self.simbolos)
		self.simb2 = random.choice(self.simbolos)
		self.simb3 = random.choice(self.simbolos)

		if self.carteira<=0:
			self.label_carteira.setText(f"Dinheiro insuficiente.")
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "❤️":
			self.carteira+=25
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🔔":
			self.carteira+=50
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍋":
			self.carteira+=100
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "🍒":
			self.carteira+=150
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "⭐":
			self.carteira+=200
		elif self.simb1 == self.simb2 and self.simb1 == self.simb2 and self.simb3 == self.simb1 and self.simb1 == "💎":
			self.carteira+=300
		else:
			self.carteira-=25

		if self.carteira>=0 and self.trava==0:
			if self.carteira == 0:
				self.trava = 1
			self.label.setText(f"{self.simb1}  {self.simb2}  {self.simb3}")
			self.label_carteira.setText(f"Sua carteira é: {self.carteira}")
		
def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()