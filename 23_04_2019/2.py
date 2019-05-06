
import numpy as np
import matplotlib.pyplot as plt


"""
? Telo se lansira sa zemlje brzinom od 10 km/s treba da iscrtamo putanju u odnosu na sunce
"""

C_AU = 1.5e11 #? Astronomska jedinica
C_T = 365.25 * 86400 #? Period zemlje oko sunca u sekundama
C_GAMMA = 6.67e-11
C_M_SUNCE = 1.98e30



def main():
    
    brzine = np.arange(5, 16, 1)

    for v in brzine: 
        
        x_0 = C_AU
        y_0 = 0
        dt = 1000
        T = 0

        x = x_0
        y = y_0

        Vxo = 0
        Vzem = 2 * np.pi * x_0 / C_T
        Vyo = Vzem + v*1e3 #? m / s

        vx = Vxo
        vy = Vyo

        m = 1

        niz_x = []
        niz_y = []


        while T < 10 * C_T:
            
            ax = -C_GAMMA * C_M_SUNCE * (x**2 + y**2)**(-3 / 2) * x
            ay = -C_GAMMA * C_M_SUNCE * (x**2 + y**2)**(-3 / 2) * y


            vx = vx + ax * dt
            vy = vy + ay * dt

            x = x + vx * dt
            y = y + vy * dt

            T = T + dt
            
            niz_x.append(x)
            niz_y.append(y)
        
        plt.plot(niz_x, niz_y)
    plt.axis("equal")
    plt.show()
        

if __name__ == "__main__":
    main()