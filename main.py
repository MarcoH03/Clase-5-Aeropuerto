import os
import time
from random import randint
import generalFunctions as gf

os.system('clear')

def main():

    #region variables

    #Areas
    sala_de_espera_1 = [] #almaceno los que estan en sala de espera y en cola para entrar a la aduana
    cola_aduana = []    #

    cabina_aduana = [None, None] #almacenaré el tiempo en el que termino de atender a los pasajeros que estan en estas cabinas

    sala_de_espera_2 = [] #almaceno los que estan en sala de espera final

    cola_frontera = [] #almaceno los que estan en cola para la frontera
    cabina_frontera = [None, None] #almacenaré el tiempo en el que termino de atender a los pasajeros que estan en estas cabinas

    #lista de pasajeros que deben abordar
    lista_pasajeros = {
        0: [ f"P_1{i}" for i in range(60) ],
        1: [f"P_2{i}" for i in range(60)]
    }

    #lista de pasajeros que deben bajar del avion
    avion = []

    #endregion viariables

    #region funcionamiento del aeropuerto

    for elapsed_time in range(601): #elapsed_time son los minutos que han pasado desde que se abre el aeropuerto
        #llegan los pasajeros y entran a la sala de espera 
        gf.pasan_a_sala_de_espera(lista_pasajeros, sala_de_espera_1, elapsed_time)

        #dos horas antes de las 11 y las 2 paso a los pasajeros de la sala de espera a la aduana y de ahi a la sala de espera 2
        gf.pasan_a_aduana(sala_de_espera_1, cola_aduana, cabina_aduana, sala_de_espera_2, elapsed_time)

        #a las 11 y a las 2 bajo a los pasajeros de los aviones que llegaron a la frontera
        gf.pasan_a_frontera(avion, cola_frontera, cabina_frontera, elapsed_time)

        #30 min antes de que salgan los vuelos empiezo a montar a los pasajeros en los aviones
        gf.pasan_al_avion(sala_de_espera_2, avion, elapsed_time)

        #actualizo en la pantalla de la terminal quines estan en cada parte del aeropuerto
        gf.estado_del_aeropuerto(sala_de_espera_1, cola_aduana, sala_de_espera_2, avion, cola_frontera, elapsed_time)
    
    #endregion funcionamiento del aeropuerto

if __name__ == "__main__":
    main()

print("")