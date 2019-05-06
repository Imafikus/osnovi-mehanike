import numpy as np 

def main():

    g = 9.81

    v0 = 100 #pocetna brzina
    
    alfa = 36 #pocetni ugao prvog hica
    
    v0_x = v0 * np.cos(np.deg2rad(alfa))
    v0_y = v0 * np.sin(np.deg2rad(alfa))


    d = 1000 #rastojanje izmedju 2 hica
    d1 = 800 #rastojanje gde treba da se sudare 2 tela
    
    dt = 0.1

    x = 0.0
    h = 0.0
    vreme_putovanja = 0.0
    v_y = None

    while(x <= d1):
        v_y = v0_y - g * vreme_putovanja
        
        dh = v_y * dt
        h += dh

        dx = v0_x * dt
        x += dx
        
        vreme_putovanja += dt

    print("Visina do koje dodje prvo telo je: ", h)
    print("Vreme putovanja: ", vreme_putovanja)
    print("Udaljenost po x osi od pocetka: ", x)


    pozicija_prvog_tela = (x, h)


    uglovi_beta = np.arange(20, 82, 2)
    brzine = np.arange(20, 210, 10)
    
    minimalna_razlika = 10e10 
    
    minimalni_par = None

    for beta in uglovi_beta:
        for u0 in brzine:

            u0_x = u0 * np.cos(np.deg2rad(beta))
            u0_y = u0 * np.sin(np.deg2rad(beta))

            pocetno_d = 1000
            trazeno_d = 800
            u_y = None
            drugo_h = 0.0
            drugo_x = 0.0
            drugo_t = 0.0

            while(pocetno_d >= trazeno_d):
                u_y = u0_y - g * dt
                dh = u_y * dt

                drugo_h += dh

                dx = u0_x * dt
                drugo_x -= dx
                
                drugo_t += dt
                pocetno_d -= dx

                rastojanje_tela = abs(np.sqrt(pozicija_prvog_tela[0]**2 + pozicija_prvog_tela[1]**2) - np.sqrt(drugo_x**2 + drugo_h**2))
            
            if(rastojanje_tela <= minimalna_razlika):
                minimalna_razlika = rastojanje_tela
                minimalni_par = (beta, u0)

    print("Minimalni par je: ", minimalni_par)



if __name__ == "__main__":
    main()