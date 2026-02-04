from mapa import Mapa
from collections import deque

class Buscador:
    def __init__(self, mapita ):
        #guardamos el objeto mapa
        self.mapa= mapita
        #lista de movimientos
        self.movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def buscar(self, inicio, salidad,usar_agua= False):
        cola = deque([inicio])
        fila= self.mapa.filas
        col= self.mapa.columnas

        # Usamos self.mapa.filas y self.mapa.columnas
        visitados= [[False for _ in range(col)] for _ in range(fila)]
        visitados[inicio[0]][inicio[1]]= True

        padres= [[None for _ in range(col)] for _ in range(fila)]
        #None= no existe

        #ciclo de busqueda 
        while cola: 
            factual, cactual= cola.popleft() #el primero que entra es primero que sale
            #fila actual, columna actual
            if (factual, cactual)== salidad:
                posi_pintar= padres[factual][cactual]
                while posi_pintar is not None and posi_pintar!= inicio:
                    pf,pc= posi_pintar
                    #pintamos con 0 el mapa original
                    self.mapa.matriz[pf][pc]="0"
                    posi_pintar= padres[pf][pc]
                return True
            
        #explorar los vecinos
            for x,y in self.movimientos:
                fnueva= x + factual
                cnueva= y + cactual

                if (0<= fnueva <fila and 0<= cnueva <col):
                    celda= self.mapa.matriz[fnueva][cnueva]
                    puede_pasar= False

                    if celda=='.' or celda == 'S' or celda=='0':
                        puede_pasar= True
                    elif celda=='A' and usar_agua: 
                        puede_pasar= True

                    if puede_pasar and not visitados[fnueva][cnueva]:
                        visitados[fnueva][cnueva]= True
                        padres[fnueva][cnueva]= (factual,cactual)
                        cola.append((fnueva,cnueva))
        return False

