from scipy.optimize import fsolve
import numpy as np
import random
import matplotlib.pyplot as plt

Gm = 0.5


def f(z,J0,a0):
    J=J0/np.sqrt(1+z**(0.25)*Gm)
    a1=a0/np.sqrt((z**0.25*Gm)**2+1)
    return z-(J/a1)**(2*a1*z**0.25-5/4)




# J0,a0,z0=0.6,1,0.5
# #print(b*z0**(1/4)-5/4)
# print(fsolve(f,z0,args=(J0,a0))[0])
# print(f(fsolve(f,z0,args=(J0,a0))[0],J0,a0))




for i in range(15000):
    #print('This is loop ',i)
    J0 = random.random()*60
    a0 = random.random()*60
    try:
        z0=0.5
        if J0<a0 :
            zsol = fsolve(f,z0,args=(J0,a0))[0]
            print(zsol)
            if zsol > 0 and zsol < 1 and abs(f(zsol,J0,a0))<0.0000001 :
                plt.scatter(J0,a0,s=1,color='green')
    except:
        continue

plt.title(r'$\Gamma$=0.5')
plt.xlabel(r'$J_0$')
plt.ylabel(r'$\alpha_0$')
plt.show()

