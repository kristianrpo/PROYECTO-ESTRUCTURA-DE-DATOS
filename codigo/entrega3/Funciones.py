import pandas as pd
import gmplot
import sys
import heapq
from collections import deque
import webbrowser
import time
from collections import deque
def calcularDistancia1(grafo, VerticeInicial,target):
    start = time.perf_counter()#Funcio para comenzar a contar el tiempo
    distancias = {Vertice: float('infinity') for Vertice in grafo} ##diccionario con cada uno de los nodos del grafo, con un valor "infinito" en cada uno de ellos.
    riesgos = {vertex: float('infinity') for vertex in grafo}##diccionario que va contener los riesgos, pero que en principio los va incializar en infinito
    riesgos[VerticeInicial] = 0
    lista_predecesores = {node: None for node in grafo}  #diccionario que guarda todos los nodos previos con valor None
    distancias[VerticeInicial] = 0 #asignación de valor (0) a la coordenada inicial del camino.
    pq = [(0,0, VerticeInicial)]#cola de prioridad la cual contiene el primer nodo en el que iniciamos nuestro camnino
    while len(pq) > 0:#mientras que la cola de prioridad no este vacia
        DistanciaActual, RiesgoActual, VerticeActual = heapq.heappop(pq)
        for Vecino, Peso in grafo[VerticeActual].items():  #empezamos a verificar la distancia minima con los vecinos.
            Distancia = DistanciaActual + (Peso[0] * Peso[1])  #se crea variable distancia la cual almacena el valor entre distancia anterior y peso del nodo actual.
            Riesgo = RiesgoActual + Peso[1]#en esta variable de riesgo se va almacenar la suma de todos los riesgo hasta el final
            if Distancia < distancias[Vecino]: #compara si la distancia de ese vecino al actual es menor a la que ya esta en el diccionario
                distancias[Vecino] = Distancia # si es menor acutuliza la distancia
                riesgos[Vecino] = Riesgo #al nodo vecino se le pone el riesgo acomulado
                lista_predecesores[Vecino] = VerticeActual#va guardar esa mejor opcion para llegar a ese vertice
                heapq.heappush(pq, (Distancia,Riesgo, Vecino)) #mete ese vecino a cola de prioridad
    end = time.perf_counter()
    ms = (end - start)
    caminoo = camino(lista_predecesores,VerticeInicial, target)
    print(f"El tiempo del primer camino es: {ms:.03f}  secs.")
    return caminoo, riesgos[target]/len(caminoo)


def calcularDistancia2(grafo, VerticeInicial,target):
    start = time.perf_counter()
    distancias = {Vertice: float('infinity') for Vertice in grafo} ##diccionario con cada uno de los nodos del grafo, con un valor "infinito" en cada uno de ellos.
    riesgos = {vertex: float('infinity') for vertex in grafo}
    riesgos[VerticeInicial] = 0
    lista_predecesores = {node: None for node in grafo}  #diccionario que guarda todos los nodos previos con valor None
    distancias[VerticeInicial] = 0 #asignación de valor (0) a la coordenada inicial del camino.
    pq = [(0,0, VerticeInicial)]
    while len(pq) > 0:
        DistanciaActual, RiesgoActual, VerticeActual = heapq.heappop(pq)
        if VerticeActual is target: break
        if DistanciaActual > distancias[VerticeActual]:
            continue

        for Vecino, Peso in grafo[VerticeActual].items():  #empezamos a verificar la distancia minima con los vecinos.
            Distancia = DistanciaActual + (Peso[0]**10*Peso[1])  #se crea variable distancia la cual almacena el valor entre distancia anterior y peso del nodo actual.
            Riesgo = RiesgoActual + Peso[1]
            if Distancia < distancias[Vecino]: #avanza en el vecino con la menor distancia.
                distancias[Vecino] = Distancia
                riesgos[Vecino] = Riesgo
                lista_predecesores[Vecino] = VerticeActual
                heapq.heappush(pq, (Distancia,Riesgo, Vecino))
    end = time.perf_counter()
    ms = (end - start)
    caminoo = camino(lista_predecesores,VerticeInicial, target)#llamamos a la funcion camino que va recibir el camino que esta en el diccionario el punto de partida y e punto inicial
    print(f"El tiempo del primer camino es: {ms:.03f}  secs.")
    return caminoo, riesgos[target]/len(caminoo)




def calcularDistancia3(grafo, VerticeInicial,target):
    start = time.perf_counter()
    distancias = {Vertice: float('infinity') for Vertice in grafo} ##diccionario con cada uno de los nodos del grafo, con un valor "infinito" en cada uno de ellos.
    riesgos = {vertex: float('infinity') for vertex in grafo}
    riesgos[VerticeInicial] = 0
    lista_predecesores = {node: None for node in grafo}  #diccionario que guarda todos los nodos previos con valor None
    distancias[VerticeInicial] = 0 #asignación de valor (0) a la coordenada inicial del camino.
    pq = [(0,0, VerticeInicial)]
    while len(pq) > 0:
        DistanciaActual, RiesgoActual, VerticeActual = heapq.heappop(pq)
        if VerticeActual is target: break
        if DistanciaActual > distancias[VerticeActual]:
            continue

        for Vecino, Peso in grafo[VerticeActual].items():  #empezamos a verificar la distancia minima con los vecinos.
            Distancia = DistanciaActual + (30*Peso[0] + 500*Peso[1])  #se crea variable distancia la cual almacena el valor entre distancia anterior y peso del nodo actual.
            Riesgo = RiesgoActual + Peso[1]
            if Distancia < distancias[Vecino]: #avanza en el vecino con la menor distancia.
                distancias[Vecino] = Distancia
                riesgos[Vecino] = Riesgo
                lista_predecesores[Vecino] = VerticeActual
                heapq.heappush(pq, (Distancia,Riesgo, Vecino))
    end = time.perf_counter()
    ms = (end - start)
    caminoo = camino(lista_predecesores,VerticeInicial, target)
    print(f"El tiempo del primer camino es: {ms:.03f}  secs.")
    return caminoo, riesgos[target]/len(caminoo)


def camino(anterior, inicio, final):
    lista_camino = deque() #lista donde guardará el camino con las coordenadas desde el punto de inicio, hasta el punto final.
    nodo_actual = final #iniciamos desde la coordenada final y nos vamos devolviendo.
    while nodo_actual != inicio: #mientras que el nodo en el que estamos sea distinto al inicial, se ejecuta (vamos de atras para adelante).
        lista_camino.append(nodo_actual)  #añadimos a la lista el nodo en el que estamos.
        nodo_actual = anterior[nodo_actual] #avanzamos al "siguiente" nodo (que en este caso, como vamos de atras para adelante, sería el anterior)
    lista_camino.append(inicio) # como el while se ejecuto hasta que encontro la posicion inicial, la posicion inicial no se guardo, así que por ultimo la almacenamos en la lista.
    lista_camino.reverse() # invertimos la lista generada ya que tiene las coordenadas al revés (ya que las almacenamos de atras para adelante)
    return lista_camino #retornamos el camino con cada una de las coordenadas desde el punto inicial hasta el final

def dibujar_mapa(lista_camino, lista_camino2, lista_camino3):
    latitud = deque() #lista de latitudes
    longitud = deque() #lista de longitudes
    latitud2 = deque()
    longitud2 = deque()
    latitud3 = deque()
    longitud3 = deque()
    for coordenada in lista_camino: #para cada una de las coordenadas en la lista, realizaremos este bloque de codigo
        coordenada = coordenada.replace(")","") #quitamos los parentesis
        coordenada = coordenada.replace("(", "")
        nueva = coordenada.split(",") #separamos el string por la coma, y nos va a quedar en la posicion 0 la longitud y en la 1 la latitud.
        latitud.append(float(nueva[1])) #guardamos la latitud como un float en la lista de latitudes
        longitud.append(float(nueva[0])) #guardamos la longitud como un float en la lista de longitudes.
    for coordenada2 in lista_camino2: #Se repite el proceso anterior para la lista 2
        coordenada2 = coordenada2.replace(")","")
        coordenada2 = coordenada2.replace("(", "")
        nueva2 = coordenada2.split(",")
        latitud2.append(float(nueva2[1]))
        longitud2.append(float(nueva2[0]))
    for coordenada3 in lista_camino3: #Se repite el proceso anterior para la lista 3
        coordenada3 = coordenada3.replace(")","")
        coordenada3 = coordenada3.replace("(", "")
        nueva3 = coordenada3.split(",")
        latitud3.append(float(nueva3[1]))
        longitud3.append(float(nueva3[0]))
    gmpOne = gmplot.GoogleMapPlotter(6.217, -75.567, 13) #creamos el mapa en la ciudad de medellin.
    gmpOne.scatter(latitud, longitud, 'red', size=9, marker=False) #generamos puntos rojos en cada una de las coordenadas (se le pasa las listas de longitud y la latitud, y el gmap los genera)
    gmpOne.plot(latitud, longitud, 'blue', edge_width=5) #unimos los puntos rojos con una linea azul, la cual va a trazar el camino, se le pasa igual las latitudes y longitudes al gmap.
    gmpOne.marker(latitud[0], longitud[0], label='A', color='orange') #hacemos un marcador para distinguir cual es el punto en el que inicia el recorrido.
    gmpOne.marker(latitud[-1], longitud[-1], label='B', color='white') #hacemos otro marcador para distinguir cual es el punto en el que finaliza el recorrido.
    gmpOne.scatter(latitud2, longitud2, 'purple', size=5, marker=False)
    gmpOne.plot(latitud2, longitud2, 'yellow', edge_width=3)
    gmpOne.scatter(latitud3, longitud3, 'black', size=5, marker=False)
    gmpOne.plot(latitud3, longitud3, 'green', edge_width=2.5)
    gmpOne.draw('mapa.html') #generamos un html con el mapa y el camino determinado.
    webbrowser.open_new_tab('mapa.html') #abrir mapa automaticamente

def crear_grafo():
    datos=pd.read_csv("calles_de_medellin_con_acoso.csv", sep=";") #leemos el csv.
    risk_media=datos["harassmentRisk"].mean() #sacamos el valor promedio del riesgo.
    datos["harassmentRisk"] = datos["harassmentRisk"].fillna(risk_media) #llenamos los espacios vacios en la columna de riesgos con el valor promedio de todos los riesgos.
    OrigenesUnicos=datos["origin"].unique() #sacamos los origenes que no se repiten.
    grafo={} #creamos el grafo.

    for i in OrigenesUnicos:
        grafo[i]={}             #guardamos como llave en el grafo todos los origenes unicos, cada uno con un diccionario vacio en su valor.

    # Se asignan los valores en el grafo, donde en el diccionario
    # que estaba vacio inicialmente en el valor, se guarda como llave
    # el destino, y como valor el acoso multplicado por la distancia de ese destino (d*r formula).
    for i in datos.index:
        if datos.oneway[i]== True: # si "oneway" es verdadero, se debe añadir en ambos sentidos al diccionario (origen->destino,destino->origen)
            try:
                grafo[datos.destination[i]][datos.origin[i]]= (datos.length[i],datos.harassmentRisk[i])               # El try y except los utilizamos cuando
            except KeyError:                                                                                        # el destino no se encuentra como origen en el grafo, y
                grafo[datos.destination[i]]={datos.origin[i]:(datos.length[i],datos.harassmentRisk[i])}               # como tratamos de acceder a algo que no existe se genera un "KeyError"
        else:                                                                                                       # para solucionarlo, añadimos el destino como una nueva llave y creamos el otro diccionario en el valor.
            grafo[datos.origin[i]][datos.destination[i]] = (datos.length[i],datos.harassmentRisk[i])
    return grafo, datos

def calcular_diferencia(camino,datos):
    acumulador_distancia = 0
    for r in range(len(camino)-1):
        largo_origen = pd.array(datos[datos['destination'] == camino[r]]['length'])
        largo_destino = pd.array(datos[datos['origin'] == camino[r+1]]['length'])
        i = 0
        j = 0
        while(i<len(largo_origen)):
            while(j<len(largo_destino)):
                if largo_origen[i]==largo_destino[j]:
                    acumulador_distancia = acumulador_distancia + largo_origen[i]
                    break
                else:
                    j+=1
            j=0
            i+=1
    return acumulador_distancia
