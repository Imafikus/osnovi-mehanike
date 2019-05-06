import numpy as np
import matplotlib.pyplot as plt


C_Ro = 1.23 #? kg/m3
Coef = 0.0001 #? koeficijent otpora
C_G = 9.81 

 
def main():

    coef_sila_otpora = 0.5 * C_Ro * Coef
    print("WTF: ", coef_sila_otpora)

    v0 = 100#? pocetna brzina
    alpha = np.deg2rad(45) #? pocetni ugao

    v0_x = v0 * np.cos(alpha)
    v0_y = v0 * np.sin(alpha)

    v_y = v0_y
    v_x = v0_x

    dt = 0.1
    y = 0
    x = 0
    t = 0

    X = []
    Y = []

    while y >= 0:
        
        X.append(x)
        Y.append(y)

        v_y = v_y - C_G*dt    
        
        x = x + v0_x * dt
        y = y + v_y * dt
        
        t = t + dt

    plt.plot(X, Y, 'r')
    
    y = 0
    x = 0
    t = 0

    X = []
    Y = []
    
    v_y = v0_y
    v_x = v0_x

    while y >= 0:
        
        X.append(x)
        Y.append(y)

        v_trenutno_2 = v_x**2 + v_y**2

        sila_otpora = coef_sila_otpora * v_trenutno_2       
 
        #print("coef sila otpora: ", coef_sila_otpora)
        #print("sila otpora: ", sila_otpora)
        v_y = v_y - C_G * dt - sila_otpora * dt    
        v_x = v_x - sila_otpora * dt
        
        x = x + v_x * dt 
        y = y + v_y * dt
        
        t = t + dt

    plt.plot(X, Y, 'b')
    plt.show()


if __name__ == "__main__":
    main()