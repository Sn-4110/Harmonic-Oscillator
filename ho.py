import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=3)
from scipy.integrate import odeint,simps
from scipy.optimize import bisect,newton


def du_dx(U,x,E):
          return [U[1],(x*x-2*E)*U[0]]


def shoot(E):
          sol=odeint(du_dx,u,x,args=(E,))
          return sol[-1][0]


N=200

En=np.linspace(0.0,6,N) # We have N possible values
#of energies from 0 to 200

x=np.linspace(-5,5,N) # Theoretically we should go to
#infinity, but for practical purpose we limit ourselves
# within a finite range of x 

u=[0.,0.001] # That is the initial condition
# We are taking psi(0)=0, dpsi_dx(0)=0.001


psif=np.zeros(N)

for i in range(N):
          psif[i] = shoot(En[i])


#print(a)

plt.plot(En,psif)
plt.ylim(-100, 200)
plt.xticks([0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5])
plt.axhline()
plt.show()



for i in range(4):
          E_n=newton(shoot,i+0.4)
          print (E_n)



          sol=odeint(du_dx,u,x,args=(E_n,))
          psi=sol[:,0]

          N= simps((psi*psi),x)

          psi_n=psi/np.sqrt(N) 
          

          la=str(i)
          la='n= ' + la
          plt.plot(x,psi_n,'o',label=la)
          plt.axhline()
          plt.legend(loc="upper left")
          
plt.show()