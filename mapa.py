import random

class Mapa:
    def __init__(self, filas, columnas):
        self.filas= filas 
        self.columnas= columnas
        #creamos el mapa
        self.matriz= [[" "for _ in range(columnas)] for _ in range(filas)]
        #Llamamos al método para que rellene la matriz
        self.obtaculos()
        
    
    def obtaculos(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                prob= random.random()
                if prob<0.2:
                    self.matriz[i][j]="A" #A= Agua
                elif prob<0.4:
                    self.matriz[i][j]="#" # '#' muro
                else:
                    self.matriz[i][j]="." # '.' camino

    #validar
    def validar(self, fila,columna):
        self.fila= fila
        self.columna= columna

        if(0<= fila< self.filas and 0<= columna< self.columnas):
            return True
        else:
            print("saliste del rango")
            return False
           

    #metodo mostrar
    def mostrar(self):
        for f in self.matriz:
            print(" ".join(f))

