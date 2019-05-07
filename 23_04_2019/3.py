
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


"""
? Telo se lansira sa zemlje brzinom od 10 km/s treba da iscrtamo putanju u odnosu na sunce 3D
"""

C_AU = 1.5e11 #? Astronomska jedinica
C_T = 365.25 * 86400 #? Period zemlje oko sunca u sekundama
C_GAMMA = 6.67e-11
C_M_SUNCE = 1.98e30



def main():
    
    brzine = np.arange(10, 15, 2)

    fig = plt.figure()
    fig.add_subplot(111, projection = "3d")

    for v in brzine: 
        print(v)
        
        x_0 = C_AU
        y_0 = 0
        z_0 = 0

        dt = 1000
        T = 0

        x = x_0
        y = y_0
        z = z_0

        Vzem = 2 * np.pi * x_0 / C_T
        Vxo = 0
        Vyo = Vzem + v*1e3 #? m / s
        Vzo = 5e3

        vx = Vxo
        vy = Vyo
        vz = Vzo

        m = 1

        niz_x = []
        niz_y = []
        niz_z = []

        while T < 100 * C_T:
            
            ax = -C_GAMMA * C_M_SUNCE * (x**2 + y**2 + z**2)**(-3 / 2) * x
            ay = -C_GAMMA * C_M_SUNCE * (x**2 + y**2 + z**2)**(-3 / 2) * y
            az = -C_GAMMA * C_M_SUNCE * (x**2 + y**2 + z**2)**(-3 / 2) * z

            vx = vx + ax * dt
            vy = vy + ay * dt
            vz = vz + az * dt

            x = x + vx * dt
            y = y + vy * dt
            z = z + vz * dt

            
            T = T + dt
        
            niz_x.append(x)
            niz_y.append(y)
            niz_z.append(z)

            
        plt.plot(niz_x, niz_y, niz_z)
        #break    
    
    plt.show()
        

if __name__ == "__main__":
    main()