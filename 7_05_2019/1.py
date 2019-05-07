
import numpy as np
import matplotlib.pyplot as plt


"""
? Kretanje tela u odnosu na Zemlju i Sunce
"""

C_AU = 1.5e11 #? Astronomska jedinica
C_T = 365.25 * 86400 #? Period zemlje oko sunca u sekundama
C_GAMMA = 6.67e-11
C_M_SUNCE = 1.99e30
C_M_ZEMLJA = 5.972 * 10**24 #? Masa Zemlje
C_R_ZEMLJA = 6.371 * 10**6 #? Poluprecnik Zemlje
SEKUNDE_GODINA = 365.25 * 86400


def main():
    
    
    W = 2 * np.pi / SEKUNDE_GODINA #? ugaona brzina zemlje
    Vz = W * C_AU #? brzina zemlje
    
    #? rastojanje satelita od zemlje
    x_g = 50 * C_R_ZEMLJA 
    y_g = 0

    #? Komponente brzine satelita
    V0y = Vz + 1000 #? km / s 30km/s je brzina zemlje
    V0x = 0

    #? udaljenost satelita od sunca na pocetku
    x_0 = C_AU + x_g
    y_0 = 0  

    #? Brzine satelita u odnosu na sunce na pocetku
    vx_h = V0x
    vy_h = V0y

    #? Vremeski korak i vreme
    dt = 1e2
    T = 0

    #? postavljamo pocetne koordinate satelita u odnosu na sunce
    x_h = x_0
    y_h = y_0

    #? ugao koji zemlja zaklapa sa x osom, koordinatni sistem fiksiran na sunce    
    lon = W*T

    niz_x = []
    niz_y = []

    while T < 2 * C_T:
        
        lon = W*T

        x_z = C_AU * np.cos(lon)
        y_z = C_AU * np.sin(lon)

        ax_h = -C_GAMMA * C_M_SUNCE * (x_h**2 + y_h**2)**(-3 / 2) * x_h -C_GAMMA * C_M_ZEMLJA* (x_g**2 + y_g**2)**(-3 / 2) * x_g
        ay_h = -C_GAMMA * C_M_SUNCE * (x_h**2 + y_h**2)**(-3 / 2) * y_h -C_GAMMA * C_M_ZEMLJA* (x_g**2 + y_g**2)**(-3 / 2) * y_g

        vx_h = vx_h + ax_h * dt
        vy_h = vy_h + ay_h * dt

        x_h = x_h + vx_h * dt
        y_h = y_h + vy_h * dt

        x_g = x_h - x_z
        y_g = y_h - y_z

        T = T + dt
        
        #print(x_h, y_h)
        niz_x.append(x_g)
        niz_y.append(y_g)
    
    plt.plot(niz_x, niz_y)
    plt.axis("equal")
    plt.show()
        

if __name__ == "__main__":
    main()