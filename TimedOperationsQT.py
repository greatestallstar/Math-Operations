import quandl
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from TimedOperationUI import Ui_Dialog

import random

class TimedOperations(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        #self.timer.display(self.Timer())
        self.pushButton.clicked.connect(self.Operations)
        self.pushButton_2.clicked.connect(self.Finished)

##    def Timer(self):
##        for i in range(5,0,-1):
##            #if i == 0:
##             #   return 0
##            print(str(i))
##            time.sleep(1)

    def Operations(self):
        number = random.randint(1,3)
        if number == 1:
            num = random.randint(1,100)
            num2 = random.randint(1,100)
            
            equation = str(num) + " + " + str(num2)
            self.textEdit.setText(equation)
            self.actualAnswer = num + num2
            
        if number == 2:
            num = random.randint(1,100)
            num2 = random.randint(1,100)
            
            equation = str(num) + " - " + str(num2) + ": "
            self.textEdit.setText(equation)
            self.actualAnswer = num - num2

        if number == 3:
            num = random.randint(1,20)
            num2 = random.randint(1,20)
            
            equation = str(num) + " x " + str(num2) + ": "
            self.textEdit.setText(equation)
            self.actualAnswer = num * num2
                
    def Finished(self):
        self.answer = int(self.plainTextEdit.toPlainText())
        if self.answer != self.actualAnswer:
            self.textEdit.setText("INCORRECT")
        else:
            self.textEdit.setText("CORRECT")

app = QApplication(sys.argv)
dialog = QtWidgets.QDialog()
widget = TimedOperations(dialog)
dialog.show()
sys.exit(app.exec_())






##import quandl
##import sys
##from PyQt5.QtCore import pyqtSlot
##from PyQt5.QtWidgets import QApplication, QDialog
##from PyQt5.uic import loadUi
##
##import random
##
##class TimedOperations(QDialog):
##    def __init__(self):
##        super(TimedOperations, self).__init__(self)
##        loadUi("TimedOperationUI.ui", self)
##        #self.timer.display(self.Timer())
##        self.pushButton.clicked.connect(self.Operations)
##        #self.pushButton_2.clicked.connect(self.Finished)
##
##    def Operations(self):
##        number = random.randint(1,3)
##        if number == 1:
##            num = random.randint(1,100)
##            num2 = random.randint(1,100)
##            
##            equation = str(num) + " + " + str(num2)
##            self.textEdit.setText(equation)
##            answer = self.plainTextEdit.toPlainText()
##            actualAnswer = num + num2
##            
##        if number == 2:
##            num = random.randint(1,100)
##            num2 = random.randint(1,100)
##            
##            equation = str(num) + " - " + str(num2) + ": "
##            self.textEdit.setText(equation)
##            answer = self.plainTextEdit.toPlainText()
##            actualAnswer = num - num2
##
##        if number == 3:
##            num = random.randint(1,20)
##            num2 = random.randint(1,20)
##            
##            equation = str(num) + " x " + str(num2) + ": "
##            self.textEdit.setText(equation)
##            answer = self.plainTextEdit.toPlainText()
##            actualAnswer = num * num2
##            
####    o = Operations(self)
####    
####    def Finished(self):
####        if o.answer == o.actualAnswer:
####            self.textEdit.setText("CORRECT")
####        else:
####            self.textEdit.setText("INCORRECT")
##
##            
##        
##app = QApplication(sys.argv)
##widget = TimedOperations()
##widget.show()
##sys.exit(app.exec_())
