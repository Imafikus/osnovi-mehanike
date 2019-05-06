import numpy as np
from math import sqrt

def euklidsko_rastojanje(x1, y1, x2, y2):

    c1 = x1**2 + y1**2
    c2 = x2**2 + y2**2
    d = sqrt(c1) - sqrt(c1)
    return abs(d)

def main():

    C_H1 = 500
    C_D = 100
    g = 9.81

    uglovi = np.arange(10, 82, 2)
    brzine = np.arange(50, 510, 10)


    min_rastojanje = 10e10
    najbolji_par = None

    for alfa in uglovi:
        for v0 in brzine:
            dt = 0.5
            predjeni_put = 0

            u0_y = 0.0
            u_y = 0.0

            v0_x = v0 * np.cos(np.deg2rad(alfa))
            v0_y = v0 * np.sin(np.deg2rad(alfa))
            v_y = v0_y

            h_drugog = C_H1
            h_ispaljenog = 0.0

            while(predjeni_put <= C_D):
                ds = v0_x * dt
                predjeni_put += ds

                u_y += g*dt
                h_drugog -= u_y * dt
                
                v_y += - g*dt
                h_ispaljenog += v_y * dt - g*dt

            rastojanje = euklidsko_rastojanje(predjeni_put, h_ispaljenog, C_D, h_drugog) 
            if rastojanje < min_rastojanje:
                min_rastojanje = rastojanje
                najbolji_par = (alfa, v0)
            

    print("Najbolji par je: ", najbolji_par)

if __name__ == "__main__":
    main()