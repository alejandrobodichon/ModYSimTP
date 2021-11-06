from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets


class Interface_globalError(QDialog):
    def __init__(self, parent=None):
        super(Interface_globalError, self).__init__(parent)
       # QDialog.setObjectName(self,"Dialog")
        self.setStyleSheet("background-color: white")
        QDialog.resize(self,1000, 550)

        #self.label_4.setGeometry(QtCore.QRect(80, 280, 55, 16))

        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas4 = FigureCanvas(self.figure)


        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton1 = QtWidgets.QPushButton()
        self.pushButton1.setObjectName("pushButton1")

        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")



        layout1 = QGridLayout()


        layout1.addWidget(self.label,1,0)
        layout1.addWidget(self.lineEdit,1,1)
        layout1.addWidget(self.label_2,2,0)
        layout1.addWidget(self.lineEdit_2,2,1)

        layout1.addWidget(self.pushButton1,7,1)
        layout1.addWidget(self.canvas4,2,3)
       #  layout.addWidget(self.canvas1,3,3)
       #  layout.addWidget(self.canvas2,5,3)
       #  layout.addWidget(self.label_9,6,0)
       # # layout.addWidget(self.canvas3,4,3)
        # adding push button to the layout

        self.setLayout(layout1)
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(self, "Global Error graphic")
        self.label_4.setText("N =")
        self.pushButton1.setText("Let\'s plot now!")
        self.label.setText("n0 =")
        self.label_2.setText("N =")
        self.pushButton1.setFixedSize(300,50)
        self.pushButton1.setStyleSheet("background-color: grey")
    def plot(self,x,arrayForErrorEuler,arrayForErrorImproved,arrayForErrorRungaKutta):
        self.figure.clear()
        plt.figure(2)
        plt.plot(x, arrayForErrorEuler, label='Euler Error')
        plt.xlabel("n")
        plt.ylabel("Error")
        plt.title('Global Error Graph')
        plt.plot(x, arrayForErrorImproved, label='Improved Euler Error')
        plt.plot(x, arrayForErrorRungaKutta, label='Runge Kutta Error')
        plt.legend()
        self.canvas4.draw()
        #self.canvas.draw()



