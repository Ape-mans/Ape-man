import math
from matplotlib import pyplot as plt
from BrentMethod import Brent
from DichotomyMethod import Dichotomy
from FibonacciMethod import Fibonacci
from GoldenRatioMethod import GoldenRatio
from ParabolicMethod import Parabolic

eps = []
resD = []
resB = []
resF = []
resG = []
resP = []
for i in range(20):
    eps.append(i)
    resD.append(Dichotomy.do_method((lambda x: x**2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 10**(-i))[1])
    resB.append(Brent.do_method((lambda x: x ** 2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 10 ** (-i))[1])
    resF.append(Fibonacci.do_method((lambda x: x ** 2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 10 ** (-i))[1])
    resG.append(GoldenRatio.do_method((lambda x: x ** 2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 10 ** (-i))[1])
    resP.append(Parabolic.do_method((lambda x: x ** 2 * math.e ** math.sin(x)), -math.pi + 0.00001, math.pi, 10 ** (-i))[1])
plt.plot(eps, resD, label="Dichotomy")
plt.plot(eps, resB, label="Brent")
plt.plot(eps, resF, label="Fibonacci")
plt.plot(eps, resG, label="GoldenRatio")
plt.plot(eps, resP, label="Parabolic")
plt.legend()
plt.xlabel('-lg(Точность)')
plt.ylabel('Кол-во итераций')
plt.show()
