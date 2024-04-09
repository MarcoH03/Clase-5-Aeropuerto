from random import randint
import os
import time

def time_in_world(elapsed_time): #me convierte el tiempo que ha pasado desde que abre el aerop en una hora real ej: 11 am
    return elapsed_time/60 + 7

def estado_del_aeropuerto(sala_de_espera_1, cola_aduana, sala_de_espera_2, avion, cola_frontera, elapsed_time): #con esta funcion voy a imprimir en columnas que pasajero esta en cada parte del aeropuerto
    os.system('clear')

    print(time_in_world(elapsed_time))
    #print("Sala de Espera 1:   Cola Aduana:   Sala de Espera 2:   Avion:   Cola Frontera:")
    print(f"Sala de Espera 1: {sala_de_espera_1}")
    print(f"Cola Aduana: {cola_aduana}")
    print(f"Sala de Espera 2: {sala_de_espera_2}")
    print(f"Avion: {avion}")
    print(f"Cola Frontera: {cola_frontera}")

    time.sleep(0.3)

    #bigest = max(len(sala_de_espera_1), len(cola_aduana), len(sala_de_espera_2), len(avion), len(cola_frontera))
    #add the while bigest > 0 print the lines with the data


def pasan_a_sala_de_espera(lista_pasajeros, sala_de_espera_1, elapsed_time): #esta funcion me va pasando a los pasajeros que llegan (random entre 0-3 a la vez) a la sala de espera
    if (time_in_world(elapsed_time) <= 8): #si estoy antes de las 4 horas para el primer vuelo
        for __ in range(randint(0,3)):
            if len(lista_pasajeros[0]) > 0:
                sala_de_espera_1.append(lista_pasajeros[0].pop(0))

    if (time_in_world(elapsed_time) >= 12 and time_in_world(elapsed_time) <= 12+1): #si estoy despues de despegar el primer avion y antes de las 4 horas para el segundo vuelo
        for __ in range(randint(0,3)):
            if len(lista_pasajeros[1]) > 0:
                sala_de_espera_1.append(lista_pasajeros[1].pop(0))
        

def pasan_a_aduana(sala_de_espera_1, cola_aduana, cabina_aduana, sala_de_espera_2, elapsed_time): #en esta funcion manejo el paso de la sala de espera 1 a la aduana a la sala de espera 2 dos horas antes de los vuelos
    if (time_in_world(elapsed_time) >= 9) and (time_in_world(elapsed_time) < 11): #si ya estamos a menos de dos horas del primer vuelo pero antes de que despuegue
        
        while len(sala_de_espera_1) > 0:
            cola_aduana.append(sala_de_espera_1.pop(0))
        
        if cabina_aduana[0] == None:
            cabina_aduana[0] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif (cabina_aduana[0] <= time_in_world(elapsed_time)) and (len(cola_aduana) > 0):
            sala_de_espera_2.append(cola_aduana.pop(0)) #si ya es la hora de terminar de atender a la persona la paso a la sala de espera 2
            cabina_aduana[0] = None

        if cabina_aduana[1] == None:
            cabina_aduana[1] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif (cabina_aduana[1] <= time_in_world(elapsed_time)) and (len(cola_aduana) > 0):
            sala_de_espera_2.append(cola_aduana.pop(0)) #si ya es la hora de terminar de atender a la persona la paso a la sala de espera 2
            cabina_aduana[1] = None


    if (time_in_world(elapsed_time) >= 12+3) and (time_in_world(elapsed_time) < 12+5): #si ya estamos a menos de dos horas del segundo vuelo pero antes de que despuegue
        while len(sala_de_espera_1) > 0:
            cola_aduana.append(sala_de_espera_1.pop(0))
        
        if cabina_aduana[0] == None:
            cabina_aduana[0] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif (cabina_aduana[0] <= time_in_world(elapsed_time)) and (len(cola_aduana) > 0):
            sala_de_espera_2.append(cola_aduana.pop(0)) #si ya es la hora de terminar de atender a la persona la paso a la sala de espera 2
            cabina_aduana[0] = None

        if cabina_aduana[1] == None:
            cabina_aduana[1] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif (cabina_aduana[1] <= time_in_world(elapsed_time)) and (len(cola_aduana) > 0):
            sala_de_espera_2.append(cola_aduana.pop(0)) #si ya es la hora de terminar de atender a la persona la paso a la sala de espera 2
            cabina_aduana[1] = None
    
    if (time_in_world(elapsed_time) == 11) or (time_in_world(elapsed_time) == 5): #si el avion ya despego' vacio la cola de la aduana
        cola_aduana = []


def pasan_a_frontera(avion, cola_frontera, cabina_frontera, elapsed_time): #en esta funcion muevo a los pasajeros qeu llegan del avion a la frontera a las horas adecuadas
    print("funcion pasan_a_frontera() no implementada")
    if (time_in_world(elapsed_time) == 11) or (time_in_world(elapsed_time) == 12+4): #si es la hora de que llegue el avion, llena la lista de los pasajeros del avion con un numero random de pasajeros
        avion = [f"A_{i}" for i in range(randint(40,60))]

    if (time_in_world(elapsed_time) == 11 + 1/60) or (time_in_world(elapsed_time) == 12+4 + 1/60) : #espero un minuto a que se abran las puertas del avion antes de bajar a los pasajeros que llegaron
        while len(avion) > 0:
            cola_frontera.append(avion.pop(0))
    
    if  (len(cola_frontera) > 0): #luego de que todos los pasajeros estan en la cola de frontera los voy atendiendo de dos en dos
        
        if cabina_frontera[0] == None:
            cabina_frontera[0] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif cabina_frontera[0] <= time_in_world(elapsed_time):
            cola_frontera.pop(0) #si ya es la hora de terminar de atender a la persona la saco del aeropuerto
            cabina_frontera[0] = None

        if cabina_frontera[1] == None:
            cabina_frontera[1] = time_in_world(elapsed_time + randint(3,10)) #si la cabina esta vacia le doy una hora a la que termino de atender a una persona
        elif (cabina_frontera[1] <= time_in_world(elapsed_time)) and (len(cola_frontera) > 0):
            cola_frontera.pop(0) #si ya es la hora de terminar de atender a la persona la saco del aeropuerto
            cabina_frontera[1] = None



def pasan_al_avion(sala_de_espera_2, avion, elapsed_time): #en esta funcion 30 min antes de los vuelos meto a los de sala de espra 2 en el avion
     if (time_in_world(elapsed_time) >= 11.5 and time_in_world(elapsed_time) < 12) or (time_in_world(elapsed_time) >= 4.5 and time_in_world(elapsed_time) < 5): #si estoy en el intervalo de abordar para alguno de los dos vuelos
         while len(sala_de_espera_2) > 0:
            avion.append(sala_de_espera_2.pop(0))
         
