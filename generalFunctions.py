from random import randint

def time_in_world(elapsed_time): #me convierte el tiempo que ha pasado desde que abre el aerop en una hora real ej: 11 am
    return elapsed_time/60 + 7

def estado_del_aeropuerto(sala_de_espera_1, cola_aduana, sala_de_espera_2, avion, cola_frontera, elapsed_time): #con esta funcion voy a imprimir en columnas que pasajero esta en cada parte del aeropuerto
    print("Sala de Espera 1:   Cola Aduana:   Sala de Espera 2:   Avion:   Cola Frontera:")

    bigest = max(len(sala_de_espera_1), len(cola_aduana), len(sala_de_espera_2), len(avion), len(cola_frontera))
    #add the while bigest > 0 print the lines with the data
        



def pasan_a_sala_de_espera(lista_pasajeros, sala_de_espera_1, elapsed_time): #esta funcion me va pasando a los pasajeros que llegan (random entre 0-3 a la vez) a la sala de espera
    if (time_in_world(elapsed_time) <= 8): #si estoy antes de las 4 horas para el primer vuelo
        for __ in range(randint(0,3)):
            if len(lista_pasajeros[0]) > 0:
                sala_de_espera_1.append(lista_pasajeros[0].pop(0))
    if (time_in_world(elapsed_time) >= 12 and time_in_world <= 1): #si estoy despues de despegar el primer avion y antes de las 4 horas para el segundo vuelo
        for __ in range(randint(0,3)):
            if len(lista_pasajeros[1]) > 0:
                sala_de_espera_1.append(lista_pasajeros[1].pop(0))
        

def pasan_a_aduana(sala_de_espera_1, cola_aduana, cabina_aduana_0, cabina_aduana_1, sala_de_espera_2, elapsed_time): #en esta funcion manejo el paso de la sala de espera 1 a la aduana a la sala de espera 2 dos horas antes de los vuelos
    print("funcion pasan_a_aduana() no implementada")

def pasan_a_frontera(avion, cola_frontera, cabina_frontera_0, cabina_frontera_1, elapsed_time): #en esta funcion muevo a los pasajeros qeu llegan del avion a la frontera a las horas adecuadas
    print("funcion pasan_a_frontera() no implementada")

def pasan_al_avion(sala_de_espera_2, avion, elapsed_time): #en esta funcion 30 min antes de los vuelos meto a los de sala de espra 2 en el avion
     print("funcion pasan_al_avio() no implementada")
