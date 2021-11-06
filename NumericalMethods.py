import math

class NumericalMethods:
    X = 0
    x0 = 0
    y0 = 0
    N = 0

    def __init__(self,x0,y0,X,N):
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.N = N

    @staticmethod
    def our_function(x, y):
        return (2 * math.exp(x) - y)
        #return (y*y + x*y - x*x)/(x*x)

    @staticmethod
    def function_for_exact_solution(x,y0,x0):
        constant = (y0 - math.exp(x0)) / math.exp(-x0)
        return math.exp(x) - math.exp(-x)*constant


    def euler_method(self):
        h = (self.X - self.x0) / self.N
        print()
        print("Now we are using Euler Method with h = ", h)
        commonArrayFor = []
        x = []
        for i in range(self.N + 1):
            x.append(self.x0 + i * h)
        y = [self.y0]
        y_exact = [self.y0]
        y_approx_through_exact = [self.y0]
        gte = [0]
        lte = [0]
        for i in range(1, self.N + 1):
            y_exact.append(self.function_for_exact_solution(x[i],self.y0,self.x0))
            y.append(y[i - 1] + h * self.our_function(x[i - 1], y[i - 1]))
            y_approx_through_exact.append(y_exact[i - 1] + h * self.our_function(x[i - 1], y_exact[i - 1]))
            lte.append(y_exact[i] - y_approx_through_exact[i])
            gte.append(y_exact[i] - y[i])
        commonArrayFor.append(x)
        commonArrayFor.append(y_exact)
        commonArrayFor.append(y)
        commonArrayFor.append(lte)
        commonArrayFor.append(gte)
        return commonArrayFor



    def improved_euler_method(self):
        h = (self.X - self.x0) / self.N
        print()
        print("Now we are using Improved Euler Method with h = ", h)
        commonArrayFor = []
        x = []
        for i in range(self.N + 1):
            x.append(self.x0 + i * h)
        y = [self.y0]
        y_exact = [self.y0]
        y_approx_through_exact = [self.y0]
        gte = [0]
        lte = [0]

        for i in range(1, self.N + 1):
            y_exact.append(self.function_for_exact_solution(x[i],self.y0,self.x0))
            k1 = self.our_function(x[i - 1], y[i - 1])
            k2 = self.our_function(x[i - 1] + h, y[i - 1] + h * k1)
            y.append(y[i - 1] + (h / 2) * (k1 + k2))

            k1_1 = self.our_function(x[i - 1], y_exact[i - 1])
            k2_1 = self.our_function(x[i - 1] + h, y_exact[i - 1] + h * k1_1)
            y_approx_through_exact.append(y_exact[i - 1] + (h / 2) * (k1_1 + k2_1))
            lte.append(y_exact[i] - y_approx_through_exact[i])
            gte.append(y_exact[i] - y[i])
        commonArrayFor.append(x)
        commonArrayFor.append(y_exact)
        commonArrayFor.append(y)
        commonArrayFor.append(lte)
        commonArrayFor.append(gte)
        return commonArrayFor

    def runge_kutta(self):
        h = (self.X - self.x0) / self.N
        print()
        print("Now we are using Runge-Kutta Method with h = ", h)
        commonArrayFor = []
        x = []
        for i in range(self.N + 1):
            x.append(self.x0 + i * h)
        y = [self.y0]
        y_exact = [self.y0]
        y_approx_through_exact = [self.y0]
        gte = [0]
        lte = [0]

        for i in range(1, self.N + 1):
            y_exact.append(self.function_for_exact_solution(x[i],self.y0,self.x0))
            k1 = self.our_function(x[i - 1], y[i - 1])
            k2 = self.our_function(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k1)
            k3 = self.our_function(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k2)
            k4 = self.our_function(x[i - 1] + h, y[i - 1] + h * k3)
            y.append(y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

            k1_1 = self.our_function(x[i - 1], y_exact[i - 1])
            k2_1 = self.our_function(x[i - 1] + h / 2, y_exact[i - 1] + (h / 2) * k1_1)
            k3_1 = self.our_function(x[i - 1] + h / 2, y_exact[i - 1] + (h / 2) * k2_1)
            k4_1 = self.our_function(x[i - 1] + h, y_exact[i - 1] + h * k3_1)
            y_approx_through_exact.append(y_exact[i - 1] + (h / 6) * (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1))
            lte.append(y_exact[i] - y_approx_through_exact[i])
            gte.append(y_exact[i] - y[i])
        commonArrayFor.append(x)
        commonArrayFor.append(y_exact)
        commonArrayFor.append(y)
        commonArrayFor.append(lte)
        commonArrayFor.append(gte)
        return commonArrayFor

