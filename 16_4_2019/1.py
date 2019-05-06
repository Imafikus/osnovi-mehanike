import numpy as np 
import matplotlib.pyplot as plt

CONST_G = 9.81
CONST_D_MESEC = 384_000_000
CONST_GAMA = 6.67e-11
CONST_M_ZEMLJA = 5.97e24
CONST_R_ZEMLJA = 6378e3
CONST_M_MESEC = CONST_M_ZEMLJA / 81.
CONST_R_MESEC = 1737e3

def main():

    dt = 1.
    niz_brzina = np.arange(10*1e3, 12 * 10e6 + 10, 10)

    niz_visina = []

    found = False

    for brzina in niz_brzina:
        if(found): break
        h = 0
        v = brzina
        print(v)

        while(v > 0 and h <= CONST_D_MESEC):
            

            if(h + v * dt >= CONST_D_MESEC): 
                print(brzina)
                found = True
                break
            
            else:
                v -= ((CONST_GAMA * CONST_M_ZEMLJA / (CONST_R_ZEMLJA + h) ** 2) - (CONST_GAMA * CONST_M_MESEC / (CONST_D_MESEC + CONST_R_MESEC- h) **2)) * dt 
                h += v * dt


if __name__ == "__main__":
    main()

