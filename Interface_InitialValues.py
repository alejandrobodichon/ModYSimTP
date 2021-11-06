from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout, QFormLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt2
from PyQt5 import QtCore, QtGui, QtWidgets


class Interface_InitialValues(QDialog):
    def __init__(self, parent=None):
        super(Interface_InitialValues, self).__init__(parent)
        QDialog.setObjectName(self,"Dialog")
        self.setStyleSheet("background-color: white")
        QDialog.resize(self,900, 800)
        self.label_4 = QtWidgets.QLabel()
        #self.label_4.setGeometry(QtCore.QRect(80, 280, 55, 16))

        self.figure1 = plt2.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure1)
        self.canvas1 = FigureCanvas(self.figure1)
        self.canvas2 = FigureCanvas(self.figure1)
        self.canvas3 = FigureCanvas(self.figure1)
        self.canvas.resize(50,50)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.MplWidget1 = QtWidgets.QWidget()

        self.MplWidget1.setObjectName("MplWidget1")
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.MplWidget3 = QtWidgets.QWidget()
        self.MplWidget3.setObjectName("MplWidget3")
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
        self.MplWidget2 = QtWidgets.QWidget()
        self.MplWidget2.setObjectName("MplWidget2")
        self.lineEdit_4 = QtWidgets.QLineEdit()
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setObjectName("label_5")

        self.label_9 = QtWidgets.QLabel()
        self.label_9.setObjectName("label_9")
       # self.MplWidget1.layout().addWidget(self.canvas)


        # adding push button to the layout

        # setting layout to the main window
        #self.setLayout(layout)
        layout = QGridLayout()


        # adding tool bar to the layout
        layout.setColumnMinimumWidth(0,5)
       # layout.setColumnStretch(1,-5)
        #layout.setColumnStretch(2,200)

        # adding canvas to the layout
        layout.addWidget(self.label,1,0)
        layout.addWidget(self.lineEdit,1,1)
        layout.addWidget(self.label_2,2,0)
        layout.addWidget(self.lineEdit_2,2,1)
        layout.addWidget(self.label_3,3,0)
        layout.addWidget(self.lineEdit_3,3,1)
        layout.addWidget(self.label_4,4,0)
        layout.addWidget(self.lineEdit_4,4,1)
        layout.addWidget(self.pushButton,7,1)
        layout.addWidget(self.canvas,1,3)
        layout.addWidget(self.canvas1,3,3)
        layout.addWidget(self.canvas2,5,3)
        layout.addWidget(self.label_9,6,0)
       # layout.addWidget(self.canvas3,4,3)
        # adding push button to the layout


        # setting layout to the main window
        self.setLayout(layout)
        #self.retranslateUi(QDialog)
       # QtCore.QMetaObject.connectSlotsByName(Ui_Dialog)

    #def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(self, "Approximation graphics")
        self.label_4.setText("N =")
        self.pushButton.setText(_translate("Dialog", "Let\'s plot!"))
        self.label_3.setText(_translate("Dialog", "X ="))
        self.label.setText(_translate("Dialog", "x0 ="))
        self.label_2.setText(_translate("Dialog", "y0 ="))
        self.label_6.setText(_translate("Dialog", "d.livitin@innopolis.university"))
        self.label_5.setText(_translate("Dialog", "Made by Daniil Livitin "))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.lineEdit_2.setText(_translate("Dialog", "0"))
        self.lineEdit_3.setText(_translate("Dialog", "7"))
        self.pushButton.setFixedSize(300,50)
        self.pushButton.setStyleSheet("background-color: grey")

    def plot(self,arrayForEuler,arrayForImproved,arrayForRungeKutta):
        self.figure1.clear()
        plt2.figure(1)
        plt2.plot(arrayForEuler[0], arrayForEuler[1])
        plt2.xlabel("x")
        plt2.ylabel("y(Exact)")
        plt2.title('Exact Graph')
        self.canvas.draw()

        self.figure1.clear()
        plt2.plot(arrayForEuler[0], arrayForEuler[1], label='Exact solution')
        plt2.plot(arrayForEuler[0], arrayForEuler[2], label='Euler')
        plt2.xlabel("x")
        plt2.ylabel("y(Approximation)")
        plt2.title('Approximation Graph')
        plt2.plot(arrayForEuler[0], arrayForImproved[2], label='Improved Euler')
        plt2.plot(arrayForEuler[0], arrayForRungeKutta[2], label='Runge Kutta')
        plt2.legend()
        self.canvas1.draw()

        self.figure1.clear()
        plt2.xlabel("x")
        plt2.ylabel("Error")
        plt2.title('Errors Graph')
        arrayForEuler[4] = [abs(ele) for ele in arrayForEuler[4]]
        arrayForImproved[4] = [abs(ele) for ele in arrayForImproved[4]]
        arrayForRungeKutta[4] = [abs(ele) for ele in arrayForRungeKutta[4]]
        plt2.plot(arrayForEuler[0], arrayForEuler[4], label='Euler Error')
        plt2.plot(arrayForEuler[0], arrayForImproved[4], label='Improved Euler Error')
        plt2.plot(arrayForEuler[0], arrayForRungeKutta[4], label='Runge Kutta Error')
        plt2.legend()
        self.canvas2.draw()

