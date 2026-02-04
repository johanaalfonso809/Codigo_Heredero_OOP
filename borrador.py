#CODIGO EN FUNCION

import random 
from collections import deque

def crear_mapa(n):
    # " #" son muros
    matriz=[[" "for _ in range(n)]for _ in range(n)]

    #generar caminos "."
    for i in range(n):
        for j in range(n):
            #devuelve un número decimal aleatorio entre 0.0 y 1.0
           prob=random.random()
           if prob <0.2:
            matriz[i][j]='A' # 
           elif prob <0.6:
            matriz[i][j]='#' #A= agua 
           else:
            matriz[i][j]= '.'
    return matriz

print("Tamaño de la matriz")
n= int(input("ingrese tamaño: "))

matriz = crear_mapa(n)

for f in matriz:
    print(" ".join(f)) 

#fe= fila entrada, ce= columna entrada 
#fs= fila saliada, cs= columna salida 
while True: 
    print("\ncoordenda de la ENTRADA")
    fe= int(input("ingrese fila: "))
    ce= int(input("ingrese columna: "))

#validar 
    if (fe<0 or fe>= n or ce< 0 or ce>=n):
        print("saliste del rango")
        continue
    if(matriz[fe][ce]=="#"):
        print("No puedes iniciar en un muro")
    else: 
        matriz[fe][ce]= "E"
        inicio= (fe, ce)
        break

#Coordena para la Salidad
while True: 
    print("\nCoordenada de salidad")
    fs= int(input("ingrese fila: "))
    cs= int(input("ingrse columna: "))

#validar que no salga del rango
    if (fs< 0 or fs>= n or cs< 0 or cs>= n):
        print("saliste del rango")
        continue
    if(matriz[fs][cs]=="#"):
        print("no puedes terminar encima de un muro")
    elif (fs== fe and cs== ce):
        print("coincide con tu entrada") 
    else: 
        matriz[fs][cs]= "S"
        salidad= (fs, cs)
        break

movimientos= [(0,1),(1,0),(0,-1),(-1,0)]


def bfs_camino(matriz, inicio, salidad, usar_agua= False):
    n= len(matriz)
    cola = deque([inicio])

    visitado=[[False]*n for _ in range(n)]
    visitado[inicio[0]][inicio[1]]= True
#padre: guarda la info como llegue a S 
#none= no existe
    padre=[[None]*n for _ in range(n)]

#ciclo de busqueda
    while cola:
        f_actual, c_actual = cola.popleft() #el primero que entra, primero sale
        if (f_actual, c_actual) == salidad:
            #reconstruimo vamos hacias atras del padre de la salida
            posi_pintar= padre[f_actual][c_actual]
            while posi_pintar is not None and posi_pintar != inicio:
                #pf= posicion fila, pc= posicion columna
                pf, pc= posi_pintar
                matriz[pf][pc]="0" 
                posi_pintar= padre[pf][pc]
            return True
        #explorar vecinos
        for f, c in movimientos:
            fnueva= f_actual + f
            cnueva= c_actual + c

            if 0<= fnueva <n and 0<= cnueva <n:
                celda= matriz[fnueva][cnueva]
                puede_pasar= False

                if celda=='.' or celda=='S' or celda=='0':
                    puede_pasar= True
                elif celda=='A' and usar_agua:
                    puede_pasar= True

                if puede_pasar is not visitado[fnueva][cnueva]:
                    visitado[fnueva][cnueva]= True
                    padre[fnueva][cnueva]=(f_actual, c_actual)
                    cola.append((fnueva, cnueva))
    return False

#llamo a mi funcion 
print("Buscar camino por tierra")
encontrado= bfs_camino(matriz,inicio,salidad, usar_agua=False)
# para que verifique si hay camino 
if not encontrado:
    print("No se encontro camino por tierra, intentado ruta alternativa por agua")
    encontrado= bfs_camino(matriz, inicio, salidad, usar_agua=True)
if encontrado:
    print('Camino mas corto')
else:
    print("no existe camino")

#imprimir 
for f in matriz:
    print(" ".join(f))

#pedir para que ingrese obstaculos
print("Responder con si o no")
while True:
    ingresar= input("desea ingresar muros: ")
    respuesta= ingresar.lower()

    if respuesta== "si": 
        #ingresar coord de muro a colocar
        fm= int(input("ingrese fila: "))
        cm= int(input("ingrese columna: "))

        if 0 <= fm < n and 0 <= cm < n:  
            print("saliste del rango")
            if (fm,cm)!= inicio and (fm,cm) != salidad:
                matriz[fm][cm]= '#'
            #limpiar camino para recalcular
            for i in range(n):
                for j in range(n):
                    if matriz[i][j]=='0':
                        matriz[i][j]=='.'
            #volver a buscar
            encontrado= bfs_camino(matriz, inicio, salidad, usar_agua=False)
            if not encontrado:
                encontrado= bfs_camino(matriz, inicio, salidad, usar_agua=True)
            for f in matriz:
                print(" ".join(f))
            print('Camino actualizao, otro muro')
    else:
        break
     
#imprension final    
print("MAPA FINAL")
for f in matriz:
    print(" ".join(f)) 