from PyQt5 import QtWidgets
import sys
from Interface_InitialValues import Interface_InitialValues
from Interface_globalError import Interface_globalError
from NumericalMethods import NumericalMethods
from GlobalError import GlobalError

class Main:
        ui = None
        ui1 = None
        def __init__(self,ui,ui1):
                self.ui = ui
                self.ui1 = ui1

        def plottingGraphsInFirstGUI(self):
                x0 = ui.lineEdit.text()
                y0 = ui.lineEdit_2.text()
                X = ui.lineEdit_3.text()
                N = ui.lineEdit_4.text()
                values = NumericalMethods(float(x0), float(y0), float(X), int(N))
                arrayForEuler = values.euler_method()
                arrayForImproved = values.improved_euler_method()
                arrayForRungaKutta = values.runge_kutta()
                ui.plot(arrayForEuler, arrayForImproved, arrayForRungaKutta)


        def plottingGraphInSecondGUI(self):
                n0 = ui1.lineEdit.text()
                N = ui1.lineEdit_2.text()
                x0 = ui.lineEdit.text()
                y0 = ui.lineEdit_2.text()
                X = ui.lineEdit_3.text()
                global_errors = GlobalError(x0,y0,X,n0,N)
                x = global_errors.calculate()[0]
                arrayForErrorsEuler = global_errors.calculate()[1]
                arrayForErrorsImproved = global_errors.calculate()[2]
                arrayForErrorsRungeKutta = global_errors.calculate()[3]
                ui1.plot(x, arrayForErrorsEuler, arrayForErrorsImproved, arrayForErrorsRungeKutta)


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ui = Interface_InitialValues()
        ui.show()

        #sys.exit(app.exec_())

        app1 = QtWidgets.QApplication(sys.argv)
        ui1 = Interface_globalError()
        ui1.show()
        main = Main(ui,ui1)
        ui.pushButton.clicked.connect(main.plottingGraphsInFirstGUI)
        ui1.pushButton1.clicked.connect(main.plottingGraphInSecondGUI)
        sys.exit(app1.exec_())







