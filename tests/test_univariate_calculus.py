import src.univariate_calculus as ucalc
import scipy.misc


print('DERIVATIVE f(x) = x^2, df/dx = 2x for x = 12')
print('My implementation:', ucalc.derivative(
    f = lambda x: x ** 2,
    x = 12))
print('Python implementation:', scipy.misc.derivative(
    func = lambda x: x ** 2,
    x0 = 12
))