import sys
import datetime
from datetime import date,datetime
from datetime import timedelta
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QButtonGroup,QPushButton,QGridLayout,QWidget

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,400,200)
		self.timer = QTimer(self)
		self.label = QLabel("",self)
		self.continua = 0

		self.botão1 = QPushButton("",self)
		self.botão2 = QPushButton("Continuar",self)
		self.botão3 = QPushButton("Parar",self)
		self.botão4 = QPushButton("Resetar",self)
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

		self.setStyleSheet("""QPushButton{font-size: 25px;
					font-family: Comic Sans Ms;
					padding: 20px;
					margin: 5px;
					border: 2px solid;}

					QPushButton:hover{
						background-color: #999e9b;
					}
					""")
		
		self.horario = datetime(2025, 5, 30, 0, 0, 0)
		self.horario2 = self.horario.strftime("%H:%M:%S")
		self.label.setText(f"{self.horario2}")

		self.label.setGeometry(88,10,530,80)
		self.label.setStyleSheet("font-size:70px; font-family: Comic Sans MS;")
		
		CW.setLayout(grid)

		self.botão2.clicked.connect(self.continuar2)
		self.botão3.clicked.connect(self.parar)
		self.botão4.clicked.connect(self.resetar)

		self.timer.timeout.connect(self.continuar)
		self.timer.start(1000)
	
	def continuar(self):
		if self.continua == 1:
			self.horario = self.horario + timedelta(seconds=1)
			self.horario2 = self.horario.strftime("%H:%M:%S")
			self.label.setText(f"{self.horario2}")

			self.label.setGeometry(88,10,530,80)
			self.label.setStyleSheet("font-size:70px; font-family: Comic Sans MS;")
	
	def continuar2(self,estado):
		if estado == False:
			self.continua = 1
			
	def parar(self):
		self.continua = 0

	def resetar(self):
		self.horario = datetime(2025,5,30,0,0,0)
		self.horario2 = self.horario.strftime("%H:%M:%S")
		self.label.setText(f"{self.horario2}")

		self.label.setGeometry(88,10,530,80)
		self.label.setStyleSheet("font-size:70px; font-family: Comic Sans MS;")
		self.continua = 0
		
def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()
