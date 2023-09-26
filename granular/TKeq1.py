from scipy.optimize import fsolve
import numpy as np
import random
import matplotlib.pyplot as plt

def f(z,a,b):
    return z-a**(1/(b*z**(1/4)-5/4))



'''
a,b,z0=0.9999,1,0.999
print(b*z0**(1/4)-5/4)
print(fsolve(f,z0,args=(a,b))[0])
print(f(fsolve(f,z0,args=(a,b))[0],a,b))

'''

for i in range(15000):
    print('This is loop ',i)
    a = random.random()
    b = random.random()*10
    try:
        z0=0.9999
        if b*z0**(1/4)-5/4>0:
            zsol = fsolve(f,z0,args=(a,b))[0]
            if zsol > 0 and zsol < 1 and abs(f(fsolve(f,z0,args=(a,b))[0],a,b))<0.0000001 :
                plt.scatter(a,b,s=1)
    except:
        continue

plt.xlabel('a')
plt.ylabel('b')
plt.show()

