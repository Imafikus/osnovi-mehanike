import numpy as np
import matplotlib.pyplot as plt


"""
? Telo se pusta sa visine H, treba izracunati kojom brzinom udari u tlo. Konstante date dole
"""

C_Ro = 1.2255 #? kg/m3 - gustina vazduha na povrsini zemlje
Coef = 0.0001 #? koeficijent otpora
C_G = 9.81 #? gravitaciona const 
M = 1 #? masa u kilogramima
H = 10 * 1000 #? pocetna visina na kojoj je telo u metrima
C_e = 2.718281
C_BC = 500. #? balisticki koeficijent (kg / mˆ2) 


def nadji_brzinu(v, otpor_vazduha):

    x_0 = H
    v_0 = 0
    dt = 1e-1
    v = v_0


    while(x_0 >= 0):
        Ro = C_Ro * C_e**(-x_0 / H)
        
        ax = (-1 / 2) * Ro * (1 / C_BC) * (v**2)

        if otpor_vazduha:
            v = v + C_G * dt + ax * dt
        
        else:
            v = v + C_G * dt



        x_0 -= v * dt

    return v

def main():


    v_bez_otpora = nadji_brzinu(0, False)
    v_sa_otporom = nadji_brzinu(0, True)

    e_bez_otpora = 1 / 2 * M * v_bez_otpora ** 2 
    e_sa_otporom = 1 / 2 * M * v_sa_otporom ** 2 

    print("OTPOR:")
    print("Brzina: ", v_bez_otpora)
    print("K. Energija: ", e_bez_otpora)
    
    print(" ")

    print("BEZ OTPORA:")
    print("Brzina: ", v_sa_otporom)
    print("K. Energija: ", e_sa_otporom)
    

    print("RAD: ", abs(e_bez_otpora - e_sa_otporom))

if __name__ == "__main__":
    main()