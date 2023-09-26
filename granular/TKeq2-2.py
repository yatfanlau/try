import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

Gm = 5

def f(z, J0, a0):
    J = J0 / np.sqrt(1 + np.abs(z) ** 0.25 * Gm)
    a1 = a0 / np.sqrt((np.abs(z) ** 0.25 * Gm) ** 2 + 1)
    return z - (J / a1) ** (2 * a1 * np.abs(z) ** 0.25 - 5 / 4)

for i in range(35000):
    J0 = random.random() * 60
    a0 = random.random() * 60
    try:
        z0 = 0.5
        if J0 < a0:
            zsol = fsolve(f, z0, args=(J0, a0))[0]
            if 0 < zsol < 1 and abs(f(zsol, J0, a0)) < 1e-7:
                plt.scatter(J0, a0, s=1, color='green')
    except:
        continue

plt.title(r'$\Gamma=5$')
plt.xlabel(r'$J_0$')
plt.ylabel(r'$\alpha_0$')
plt.show() 
