from NumericalMethods import NumericalMethods
class GlobalError:
    def __init__(self,x0,y0,X,n0,N):
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.n0 = n0
        self.N = N
    def calculate(self):
        arrayForErrorsEuler = []
        arrayForErrorsImproved = []
        arrayForErrorsRungeKutta = []
        x = []
        for i in range(int(self.n0), int(self.N) + 1):
            values = NumericalMethods(float(self.x0), float(self.y0), float(self.X), int(i))
            arrayForEuler = values.euler_method()
            arrayForImproved = values.improved_euler_method()
            arrayForRungaKutta = values.runge_kutta()
            arrayForEuler[4] = [abs(ele) for ele in arrayForEuler[4]]
            arrayForImproved[4] = [abs(ele) for ele in arrayForImproved[4]]
            arrayForRungaKutta[4] = [abs(ele) for ele in arrayForRungaKutta[4]]
            arrayForErrorsEuler.append(max(arrayForEuler[4]))
            arrayForErrorsImproved.append(max(arrayForImproved[4]))
            arrayForErrorsRungeKutta.append(max(arrayForRungaKutta[4]))
            x.append(i)
        commonArray = []
        commonArray.append(x)
        commonArray.append(arrayForErrorsEuler)
        commonArray.append(arrayForErrorsImproved)
        commonArray.append(arrayForErrorsRungeKutta)
        return commonArray
