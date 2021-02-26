print ("¿Cuántos planetas desea subir al sistema?")
numPlanets = int(input())
coords = [0]*numPlanets*2
masas = [0]*numPlanets
campos = [0]*numPlanets*2
puntoa = [0]*2
cont = 0

for i in range (numPlanets):
    print("Dame los datos del planeta ", i+1)
    for j in range (2):
        print("Coordenada ", j+1)
        coords[cont] = int(input())
        cont = cont +1
    print("Dame la masa del planeta",i+1)
    masas[i] = int(input())


print("Dame el punto a analizar")
for i in range(2):
    print("Coordenada ", i+1)
    puntoa[i] = int(input())

cont = 0
campox = 0
campoy = 0

for i in range(numPlanets):
    if(coords[cont] - puntoa[0]) != 0:
        C1 = (masas[i]*(coords[cont] - puntoa[0]))/(coords[cont]-puntoa[0]).__abs__().__pow__(2)
        campox = campox + C1
    cont = cont+1
    if (coords[cont] - puntoa[1]) != 0:
        C2 =(masas[i]*(coords[cont] - puntoa[1]))/(coords[cont]-puntoa[1]).__abs__().__pow__(2)
        campoy = campoy +C2
    cont = cont+1

print("Campo Gravitacional: G * ( ", campox, "," ,campoy, ")")

campoxfin = campox*4
campoyfin = campoy*4

print("Campo Gravitacional con masa de 4kg: G * ( ", campoxfin, "," ,campoyfin, ")")

