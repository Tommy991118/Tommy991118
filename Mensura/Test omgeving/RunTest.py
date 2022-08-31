from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
import sys
import mainTest
import pyautogui as py

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400,400,850,350) 
        self.setWindowTitle("Gevarenlijst inputten") 
        
        self.label = QLabel(self)
        self.label.setText("Voorbereidingen voor het script:")
        self.label.setFont(QtGui.QFont("Arial", 20))
        self.label.move(50,40) 
        self.label.adjustSize()

        self.label2 = QLabel(self)
        self.label2.setText(
             " -Het script moet runnen op een Dell laptop zonder aanpassingen aan de resolutie (Default: 1920x1080). \
             \n \n -Open een Word document, zet deze op full screen en 116% zoom level. Sluit daarna het Word document.\
             \n \n -Het opgevraagd aantal bedrijfsbezoeken (records) moet meer dan 20 zijn, dus gelieve geen korte tijdperiode op te vragen. \
             \n -Het wordt aangeraden om buiten dit programma niks anders open te hebben staan zodat niks in de weg komt te staan. \
             \n \n SCRIPT STOPPEN: de muis naar linksboven bewegen tot het in de hoek zit. Deze positie van de muis moet behouden worden tot \
             \n de Python logo van de taakbalk verdwijnt. Dat indiceert dat het script is gestopt.\
             \n\n Opmerkingen: \
             \n -De datums moeten manueel ingegeven worden, hier wordt 20 seconden voor voorzien wanneer het script op de het input veld van de datums klikt.\
             \n Het sorteren van de datums van recent naar later moet ook manueel gedaan worden.")
        self.label2.move(60,100)
        self.label2.adjustSize()

        self.b1 = QPushButton(self)
        self.b1.setText("Start")
        self.b1.move(80,250)
        self.b1.setGeometry(300,280,200,50)
        self.b1.clicked.connect(self.button_clicked)

    def button_clicked(self):
        msg = QMessageBox()
        msg.setWindowTitle("")
        msg.setText("Gelieve de muis zo min mogelijk aan te raken nadat u op 'ok' hebt geklikt.")
        x = msg.exec_()
        msg.setIcon(QMessageBox.Critical)
        #Start script
        mainTest.start()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()