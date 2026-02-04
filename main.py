from mapa import Mapa
from bfs_buscador import Buscador
def main():
    print("---Ingresar tamaño del Mapa---")
    filas= int(input("ingrese numero de filas: "))
    columnas= int(input("ingrese numero de columnas: "))

    #creamos el objeto mapa
    mi_mapa= Mapa(filas, columnas)

    #usamos el metodo
    mi_mapa.mostrar()
    #pedir inicio validar y colocar en el mapa
    while True: 
        fini= int(input("ingrese fila inicio: "))
        cini= int(input("ingrese columna inicio: "))

        valido= mi_mapa.validar(fini, cini)
        if valido== False:
            print("saliste del rango")
            continue
        elif mi_mapa.matriz[fini][cini] == "#" or mi_mapa.matriz[fini][cini]=="A":
            print("no puedes iniciar en un muro o Agua")   
        else:
            mi_mapa.matriz[fini][cini]="E"
            inicio = (fini, cini)
            break

    #salidad
    while True: 
        fsal= int(input("ingrese fila salidad: "))
        csal= int(input("ingrese columna salidad: "))

        valido= mi_mapa.validar(fsal,csal)
        if valido== False:
            print("Saliste del rango")
            continue
        elif mi_mapa.matriz[fsal][csal] =="#" or mi_mapa.matriz[fsal][csal]=="A":
            print("No puedes terminar en muro o Agua")
        else: 
            mi_mapa.matriz[fsal][csal]="S"
            salidad= (fsal, csal)
            break

    #busco
    print('Buscar camino por tierra')
    busca= Buscador(mi_mapa)
    encontrado= busca.buscar(inicio,salidad,usar_agua= False)
    if not encontrado:
        print("No se encontro camino por tierra, intentado ruta alternativa por agua")
        encontrado= busca.buscar(inicio,salidad,usar_agua= True)
    if encontrado:
        print("Camino mas corto")
    else: 
        print("no existe camino")

    mi_mapa.mostrar()

    print("Responder con si o no")
    while True: 
        ingresar= input("desea agregar obstaculos: ")
        repuesta= ingresar.lower()

        if repuesta== "si":
            fo= int(input("ingrese fila: "))
            co= int(input("ingrese columna: "))

            vale= mi_mapa.validar(fo,co)
            if vale== False:
                print("saliste del rango")
                continue
            if (fo,co)!= salidad and (fo,co)!= inicio :
                mi_mapa.matriz[fo][co]="#"
                #limpiar camino para recalcular 
                for i in range(mi_mapa.filas):
                    for j in range(mi_mapa.columnas):
                        if mi_mapa.matriz[i][j]=="0":
                            mi_mapa.matriz[i][j]="."
                #volver a buscar camino
                encontrado= busca.buscar(inicio, salidad, usar_agua=False)
                if not encontrado:
                    encontrado= busca.buscar(inicio,salidad,usar_agua= True)
                if encontrado:
                    print("Camino mas corto")
                else: 
                    print("no existe camino")
                
                mi_mapa.mostrar()
        else:
            print("Mapa final")
            mi_mapa.mostrar()
            break
            
if __name__ == "__main__":
    main()