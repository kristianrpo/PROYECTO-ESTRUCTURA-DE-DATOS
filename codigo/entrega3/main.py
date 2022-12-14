from Funciones import dibujar_mapa, calcularDistancia1, calcularDistancia2, calcularDistancia3, camino, crear_grafo, calcular_diferencia


def main():
    while True:
        grafo,datos = crear_grafo()
        print("Ingese el numero según la ruta que desea recorrer: ")
        print("1. Del Palacio de bellas artes a la Unidad deportiva castilla: ")
        print("2. De la Cancha Belén las Violetas a la Cancha Sintetica Uva Sol De Oriente Comuna 8: ")
        print("3. De Estadio Atanasio Girardot al Autoservicio San Luis: ")
        print("4. De la Universidad Pontificie Bolivariana a el Jardín infantil buen comienzo La Colina: ")
        print("5. De la Universidad EAFIT a la Universidad Nacional : ")
        print("6. Salir")
        numero_control = int(input())
        if numero_control == 1:
            anteriores1, riesgo1= calcularDistancia1(grafo, '(-75.5617431, 6.2496046)', '(-75.572654, 6.297935)')
            anteriores2,riesgo2 = calcularDistancia2(grafo, '(-75.5617431, 6.2496046)', '(-75.572654, 6.297935)')
            anteriores3,riesgo3 = calcularDistancia3(grafo, '(-75.5617431, 6.2496046)', '(-75.572654, 6.297935)')
            dibujar_mapa(anteriores1, anteriores2, anteriores3)
            print("")
            print("La distancia calculada fué: ")
            print("primer camino (azul: d*r): ", calcular_diferencia(anteriores1, datos))
            print("segundo camino (amarillo: d**10*r): ", calcular_diferencia(anteriores2, datos))
            print("tercer camino (verde: 30*d+500*r): ", calcular_diferencia(anteriores3, datos))
            print("")
            print("el riesgo total calculado fué: ")
            print("primer camino (azul: d*r): ", riesgo1)
            print("segundo camino (amarillo: d**10*r): ", riesgo2)
            print("tercer camino (verde: 30*d+500*r): ", riesgo3)
            print("")
        if numero_control == 2:
            anteriores1, riesgo1= calcularDistancia1(grafo, '(-75.6149077, 6.2345234)', '(-75.5405454, 6.244039)')
            anteriores2,riesgo2= calcularDistancia2(grafo, '(-75.6149077, 6.2345234)', '(-75.5405454, 6.244039)')
            anteriores3,riesgo3= calcularDistancia3(grafo, '(-75.6149077, 6.2345234)', '(-75.5405454, 6.244039)')
            dibujar_mapa(anteriores1,anteriores2,anteriores3)
            print("")
            print("La distancia calculada fué: ")
            print("primer camino (azul: d*r): ", calcular_diferencia(anteriores1, datos))
            print("segundo camino (amarillo: d**10*r): ", calcular_diferencia(anteriores2, datos))
            print("tercer camino (verde: 30*d+500*r): ", calcular_diferencia(anteriores3, datos))
            print("")
            print("el riesgo total calculado fué: ")
            print("primer camino (azul: d*r): ", riesgo1)
            print("segundo camino (amarillo: d**10*r): ", riesgo2)
            print("tercer camino (verde: 30*d+500*r): ", riesgo3)
            print("")
        if numero_control == 3:
            anteriores1, riesgo1= calcularDistancia1(grafo, '(-75.5879543, 6.2568545)', '(-75.5473578, 6.2689824)')
            anteriores2, riesgo2= calcularDistancia2(grafo, '(-75.5879543, 6.2568545)', '(-75.5473578, 6.2689824)')
            anteriores3,riesgo3= calcularDistancia3(grafo, '(-75.5879543, 6.2568545)', '(-75.5473578, 6.2689824)')
            dibujar_mapa(anteriores1,anteriores2,anteriores3)
            print("")
            print("La distancia calculada fué: ")
            print("primer camino (azul: d*r): ", calcular_diferencia(anteriores1, datos))
            print("segundo camino (amarillo: d**10*r): ", calcular_diferencia(anteriores2, datos))
            print("tercer camino (verde: 30*d+500*r): ", calcular_diferencia(anteriores3, datos))
            print("")
            print("el riesgo total calculado fué: ")
            print("primer camino (azul: d*r): ", riesgo1)
            print("segundo camino (amarillo: d**10*r): ", riesgo2)
            print("tercer camino (verde: 30*d+500*r): ", riesgo3)
            print("")
        if numero_control == 4:
            anteriores1,riesgo1= calcularDistancia1(grafo, '(-75.5901471, 6.2446104)', '(-75.5892882, 6.1995555)')
            anteriores2,riesgo2= calcularDistancia2(grafo, '(-75.5901471, 6.2446104)', '(-75.5892882, 6.1995555)')
            anteriores3,riesgo3= calcularDistancia3(grafo, '(-75.5901471, 6.2446104)', '(-75.5892882, 6.1995555)')
            dibujar_mapa(anteriores1,anteriores2,anteriores3)
            print("")
            print("La distancia calculada fué: ")
            print("primer camino (azul: d*r): ", calcular_diferencia(anteriores1, datos))
            print("segundo camino (amarillo: d**10*r): ", calcular_diferencia(anteriores2, datos))
            print("tercer camino (verde: 30*d+500*r): ", calcular_diferencia(anteriores3, datos))
            print("")
            print("el riesgo total calculado fué: ")
            print("primer camino (azul: d*r): ", riesgo1)
            print("segundo camino (amarillo: d**10*r): ", riesgo2)
            print("tercer camino (verde: 30*d+500*r): ", riesgo3)
            print("")
        if numero_control ==5:
            anteriores1, riesgo1= calcularDistancia1(grafo, '(-75.5790173, 6.1971336)', '(-75.5762232, 6.266327)')
            anteriores2, riesgo2= calcularDistancia2(grafo, '(-75.5790173, 6.1971336)', '(-75.5762232, 6.266327)')
            anteriores3, riesgo3= calcularDistancia3(grafo, '(-75.5790173, 6.1971336)', '(-75.5762232, 6.266327)')
            dibujar_mapa(anteriores1,anteriores2,anteriores3)
            print("")
            print("La distancia calculada fué: ")
            print("primer camino (azul: d*r): ", calcular_diferencia(anteriores1, datos))
            print("segundo camino (amarillo: d**10*r): ", calcular_diferencia(anteriores2, datos))
            print("tercer camino (verde: 30*d+500*r): ", calcular_diferencia(anteriores3, datos))
            print("")
            print("el riesgo total calculado fué: ")
            print("primer camino (azul: d*r): ", riesgo1)
            print("segundo camino (amarillo: d**10*r): ", riesgo2)
            print("tercer camino (verde: 30*d+500*r): ", riesgo3)
            print("")
        if numero_control == 6:
            break
main()
