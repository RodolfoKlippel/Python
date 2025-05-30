import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(700,300,510,200)
		self.timer = QTimer(self)
		self.label = QLabel("",self)
		
		self.timer.timeout.connect(self.initUI)
		self.timer.start(1000)
		
	def initUI(self):
		self.horario = datetime.datetime.now()
		self.horario = self.horario.strftime("%H:%M:%S %p")
		self.label.setText(f"{self.horario}")

		self.label.setGeometry(10,10,530,160)
		self.label.setStyleSheet("font-size:80px; font-family: Comic Sans MS;")
		
def main():
	aplicativo = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(aplicativo.exec_())
	
if __name__ == "__main__":
	main()
