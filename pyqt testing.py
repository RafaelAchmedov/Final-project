from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
   def __init__(self):
      super(MyWindow, self).__init__()
      self.setGeometry(1500, 350, 500, 600)
      self.setWindowTitle("Techasas with Rafa")
      self.initUI()

   def initUI(self):
      self.label = QtWidgets.QLabel(self)
      self.label.setText("Rafa first Label")
      self.label.move(50, 50)

      self.b1 = QtWidgets.QPushButton(self)
      self.b1.setText("Click me Please")
      self.b1.clicked.connect(self.clicked)


   def update(self):
      self.label.adjustSize()

   def clicked(self):
      self.label.setText("You pressed the button")
      self.update()


def clicked():
   print("Clicked yesy esy esy esyeyese")


def window():
   app = QApplication(sys.argv)
   win = MyWindow()
   win.show()
   sys.exit(app.exec())

window()