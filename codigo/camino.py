import pandas as pd
import gmplot
import sys
datos=pd.read_csv("calles_de_medellin_con_acoso.csv",sep=";") #leemos el csv.
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
            grafo[datos.destination[i]][datos.origin[i]]= datos.length[i]*datos.harassmentRisk[i]               # El try y except los utilizamos cuando
        except KeyError:                                                                                        # el destino no se encuentra como origen en el grafo, y
            grafo[datos.destination[i]]={datos.origin[i]:datos.length[i]*datos.harassmentRisk[i]}               # como tratamos de acceder a algo que no existe se genera un "KeyError"
    else:                                                                                                       # para solucionarlo, añadimos el destino como una nueva llave y creamos el otro diccionario en el valor.
        grafo[datos.origin[i]][datos.destination[i]] = datos.length[i]* datos.harassmentRisk[i]

def dijkstra(grafo, inicio):
    distancias_cortas = {node: float('inf') for node in grafo} #diccionario con cada uno de los nodos del grafo, con un valor "infinito" en cada uno de ellos.
    distancias_cortas[inicio] = 0                              #asignación de valor (0) a la coordenada inicial del camino.
    lista_predecesores = {node: None for node in grafo}        #diccionario que guarda todos los nodos previos con valor None
    nodos_visitados = []                                       #lista vacia en la que se almacenaran las coordenadas que el algoritmo ya ha recorrido.
    nodos_sin_visitar = list(grafo.keys())                     #lista que contiene todos los "nodos" o coordenadas del grafo.

    while nodos_sin_visitar: #mientras que aún existen nodos o coordenadas se va a ejecutar lo que esté dentro del while.
        nodo_actual = min(nodos_sin_visitar, key=lambda node: distancias_cortas[node]) #el nodo actual será igual al nodo con la menor distancia calculada anteriormente.
        nodos_sin_visitar.remove(nodo_actual) #elimina el nodo actual de nodos sin visitar.
        nodos_visitados.append(nodo_actual)   #agrega el nodo actual a nodos que ya fueron visitados.
        for node in grafo[nodo_actual]:       #empezamos a verificar la distancia minima con los vecinos.
            if node not in nodos_visitados:   #verificar si el nodo ya fue visitado (para no volver a verificar).
                distancia = distancias_cortas[nodo_actual] + grafo[nodo_actual][node] #se crea variable distancia la cual almacena el valor entre distancia anterior y peso del nodo actual.
                if distancia < distancias_cortas[node]: #avanza en el vecino con la menor distancia.
                    distancias_cortas[node] = distancia
                    lista_predecesores[node] = nodo_actual
    return distancias_cortas, lista_predecesores    #finalmente, retorna el camino con las distancias mas cortas en absolutamente todos los nodos del grafo.

def camino(anterior, inicio, final):
    lista_camino = [] #lista donde guardará el camino con las coordenadas desde el punto de inicio, hasta el punto final.
    nodo_actual = final #iniciamos desde la coordenada final y nos vamos devolviendo.
    while nodo_actual != inicio: #mientras que el nodo en el que estamos sea distinto al inicial, se ejecuta (vamos de atras para adelante).
        lista_camino.append(nodo_actual)  #añadimos a la lista el nodo en el que estamos.
        nodo_actual = anterior[nodo_actual] #avanzamos al "siguiente" nodo (que en este caso, como vamos de atras para adelante, sería el anterior)
    lista_camino.append(inicio) # como el while se ejecuto hasta que encontro la posicion inicial, la posicion inicial no se guardo, así que por ultimo la almacenamos en la lista.
    lista_camino.reverse() # invertimos la lista generada ya que tiene las coordenadas al revés (ya que las almacenamos de atras para adelante)
    return lista_camino #retornamos el camino con cada una de las coordenadas desde el punto inicial hasta el final

def dibujar_mapa(lista_camino):
    latitud = [] #lista de latitudes
    longitud = [] #lista de longitudes
    for coordenada in lista_camino: #para cada una de las coordenadas en la lista, realizaremos este bloque de codigo
        coordenada = coordenada.replace(")","") #quitamos los parentesis
        coordenada = coordenada.replace("(", "")
        nueva = coordenada.split(",") #separamos el string por la coma, y nos va a quedar en la posicion 0 la longitud y en la 1 la latitud.
        latitud.append(float(nueva[1])) #guardamos la latitud como un float en la lista de latitudes
        longitud.append(float(nueva[0])) #guardamos la longitud como un float en la lista de longitudes.
    gmpOne = gmplot.GoogleMapPlotter(6.217, -75.567, 13) #creamos el mapa en la ciudad de medellin.
    gmpOne.scatter(latitud, longitud, 'red', size=5, marker=False) #generamos puntos rojos en cada una de las coordenadas (se le pasa las listas de longitud y la latitud, y el gmap los genera)
    gmpOne.plot(latitud, longitud, 'blue', edge_width=2.5) #unimos los puntos rojos con una linea azul, la cual va a trazar el camino, se le pasa igual las latitudes y longitudes al gmap.
    gmpOne.marker(latitud[0], longitud[0], label='A', color='yellow') #hacemos un marcador para distinguir cual es el punto en el que inicia el recorrido.
    gmpOne.marker(latitud[-1], longitud[-1], label='B', color='green') #hacemos otro marcador para distinguir cual es el punto en el que finaliza el recorrido.
    gmpOne.draw('mapa.html') #generamos un html con el mapa y el camino determinado.


distancias, anteriores = dijkstra(grafo, '(-75.609497, 6.2581403)')
lista_camino = camino(anteriores, '(-75.609497, 6.2581403)', '(-75.6348967, 6.2704309)')
print(lista_camino)
dibujar_mapa(lista_camino)
