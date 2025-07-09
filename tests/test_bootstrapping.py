import src.bootstrapping as b
import numpy as np


data = [ round( float(value), 3 ) for value in np.random.uniform(
    low = 1,
    high = 10,
    size = 8
) ]

print('======BOOTSTRAPPING======')
print('Original Dataset:', sorted(data))
print('Bootstrapp iteration 1:', sorted(b.bootstrapp(
    data = data
)))
print('Bootstrapp iteration 2:', sorted(b.bootstrapp(
    data = data
)))
print('Bootstrapp iteration 3:', sorted(b.bootstrapp(
    data = data
)))
print('Bootstrapp iteration 4:', sorted(b.bootstrapp(
    data = data
)))
print('Bootstrapp iteration 5:', sorted(b.bootstrapp(
    data = data
)))