import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['backend'] = "Qt4Agg"

C_GAMA = 6.67 * 10**(-11) 
C_M = 5.972 * 10**24 #? Masa Zemlje
C_R = 6.371 * 10**6 #? Poluprecnik Zemlje

T = []

def main():
    dt = 1. #? vremenski korak
    v0 = 2000 #? pocetna brzina

    const = dt * C_GAMA * C_M / C_R**2 #? konstanta
    spec_dt = dt #? ono ce se menjati dinamicki
    
    h0 = 0 #? pocetna visina 

    brzine = np.arange(100, 12000, 100)
    
    for v0 in brzine:

        h = h0
        v = v0
        t = 0
        spec_t = 0

        while(v > 0):
            a = C_GAMA  * C_M / ((C_R + h)**2)
            
            v = v - a*dt
            
            h = h + v * dt
            
            t = t + dt

            
        #print("Visina do koje dodje je: ", h)

        spec_V = v0
        spec_h = h0
        
        while(spec_V > 0):
            a = C_GAMA  * C_M / ((C_R + spec_h)**2)

            spec_V = spec_V - a * spec_dt

            spec_h = spec_h + spec_V * spec_dt

            spec_dt = const / a
            spec_t = spec_t + spec_dt
        
        #print("Visina do koje dodje specijalno:", spec_h)


        #print("v0: ", v0, "t: ", t, "spec_t: ", spec_t)
        #print("\n")
        
        T.append(t / spec_t)

    plt.plot(brzine, T, '-r')
    plt.show()


if __name__ == "__main__":
    main()