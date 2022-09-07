
from re import X
from NodoCabeza import NodoCabeza
from ListaHead import ListaHead
from Celda import Celda
# from NodoCelda import NodoCelda
import os 
import webbrowser

class NodoCelda(): 
    def __init__(self, x, y, dato):
        self.dato = dato
        self.coordenadaX = x  
        self.coordenadaY = y  
        self.arriba = None
        self.abajo = None
        self.derecha = None  
        self.izquierda = None  

    def setArriba(self, arriba):
        
        self.arriba = arriba
    
    def getArriba(self):
        
        return self.arriba
    
    def setAbajo(self, abajo):
        
        self.abajo = abajo
    
    def getAbajo(self):
       
        return self.abajo

    def setDerecha(self, derecha):
        
        self.derecha = derecha
    
    def getDerecha(self):
        
        return self.derecha
    
    def setIzquierda(self, izquierda):
        
        self.izquierda = izquierda
    
    def getIzquierda(self):
        
        return self.izquierda
    
    def setDato(self, dato):
        
        self.dato = dato
    
    def getDato(self):
        
        return self.dato

class MatrizDispersa():
    def __init__(self):
        self.numeroFilas = 0
        self.numeroColumnas = 0
        self.filas = ListaHead('fila')
        self.columnas = ListaHead('columna')


    def insertar(self, posx, posy, dato):
        nuevaCelda = NodoCelda(posx,posy,dato)
        nodoX = self.filas.getCabeza(posx)
        nodoY = self.columnas.getCabeza(posy)

        if nodoX == None:

            self.numeroFilas += 1
            nodoX = NodoCabeza(posx)
            self.filas.insertarNodoCabeza(nodoX)

        if nodoY == None:
            self.numeroColumnas += 1
            nodoY = NodoCabeza(posy)
            self.columnas.insertarNodoCabeza(nodoY)

        if nodoX.getAcceso() == None:
            nodoX.setAcceso(nuevaCelda)
        else:
            if nuevaCelda.coordenadaY < nodoX.getAcceso().coordenadaY:
                nuevaCelda.setDerecha(nodoX.getAcceso())
                nodoX.getAcceso().setIzquierda(nuevaCelda)
                nodoX.setAcceso(nuevaCelda)
            else:
                tmp: NodoCelda = nodoX.getAcceso()

                while tmp != None:
                    if nuevaCelda.coordenadaY < tmp.coordenadaY:
                        nuevaCelda.setDerecha(tmp)
                        nuevaCelda.setIzquierda(tmp.getIzquierda())
                        tmp.getIzquierda().setDerecha(nuevaCelda)
                        tmp.setIzquierda(nuevaCelda)
                        break
                    elif nuevaCelda.coordenadaX == tmp.coordenadaX and nuevaCelda.coordenadaY == tmp.coordenadaY:
                        break
                    else:
                        if tmp.getDerecha() == None:
                            tmp.setDerecha(nuevaCelda)
                            nuevaCelda.setIzquierda(tmp)
                            break
                        else:
                            tmp = tmp.getDerecha()
            
        
        if nodoY.getAcceso() == None:
            nodoY.setAcceso(nuevaCelda)
        else:
            if nuevaCelda.coordenadaX < nodoY.getAcceso().coordenadaX:
                nuevaCelda.setAbajo(nodoY.getAcceso())
                nodoY.getAcceso().setArriba(nuevaCelda)
                nodoY.setAcceso(nuevaCelda)

            else:   
                tmp2: NodoCelda = nodoY.getAcceso()

                while tmp2 != None:

                    if nuevaCelda.coordenadaX < tmp2.coordenadaX:
                            nuevaCelda.setAbajo(tmp2)
                            nuevaCelda.setArriba(tmp2.getArriba())
                            tmp2.getArriba().setAbajo(nuevaCelda)
                            tmp2.setArriba(nuevaCelda)
                            break
                    elif nuevaCelda.coordenadaX == tmp2.coordenadaX and nuevaCelda.coordenadaY == tmp2.coordenadaY:
                        break
                    else:
                        if tmp2.getAbajo() == None:
                            tmp2.setAbajo(nuevaCelda)
                            nuevaCelda.setArriba(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getAbajo()


    def recorridoFila(self, fila):
        inicio : NodoCabeza = self.filas.getCabeza(fila)
        if inicio == None:
            return None
            
        tmp : NodoCelda = inicio.getAcceso()
        
        while tmp != None:
            print('('+ str(tmp.coordenadaX) + ', '+ str(tmp.coordenadaY) + ') ' +' '+ str(tmp.dato.getIdCelda()) + ' coordenada: ' + str(tmp.dato.getX()) + '  ' + str(tmp.dato.getY()) + ' Color: ' + tmp.dato.getColor())  
            tmp = tmp.getDerecha()
        
    def recorridoColumna(self, columna):
    
        inicio : NodoCabeza = self.columnas.getCabeza(columna)
        if inicio == None:

            return None

        tmp : NodoCelda = inicio.getAcceso()
        
        while tmp != None:
            print('('+ str(tmp.coordenadaX) + ', '+ str(tmp.coordenadaY) + ') ' + tmp.dato )
            tmp = tmp.getAbajo()

    
    def mostrarMatriz(self):
     
        inicio = self.filas.primero.id
        final = self.filas.ultimo.id
        print(inicio)
        print(final)
        i = inicio

        for j  in range(inicio, final + 1):

            self.recorridoFila(i)

            i +=  1
     
    def actualizarDato(self, posx, posy, dato):
        
        nuevaCelda = NodoCelda(posx, posy, dato)
        
        # print('=======')
        # print(nuevaCelda)
        # print('=======')
        nodo_X = self.filas.getCabeza(posx)
        # nodo_Y = self.columnas.getCabeza(posy)
        
        # Actualizar en fila
        print(nodo_X)
        # print(posx)
        x=nodo_X.getAcceso().coordenadaY
        print(nodo_X.getAcceso().coordenadaY)
        if nuevaCelda.coordenadaY == x:
        # if nuevaCelda.coordenadaY == nodo_X.getAcceso().coordenadaY:
            
            nodo_X.getAcceso().setDato(nuevaCelda.getDato())
        else:
            
            temp = nodo_X.getAcceso()
            
            while temp != None:
                
                if nuevaCelda.coordenadaY == temp.coordenadaY:
                    
                    temp.setDato(nuevaCelda.getDato())
                
                temp = temp.getDerecha()

    
    def extremos_nodoCabeceraFila(self):
        
        return  (self.filas.getPrimerNodo(),self.filas.getUltimoNodo())
    
    def extremos_nodoCabeceraColumna(self):
        
        return (self.columnas.getPrimerNodo(),self.columnas.getUltimoNodo())



    def graficarMapa(self, nombrePaciente, filas, columnas): 

            graphviz = 'digraph L{ \n node[shape= square, fillcolor="#C0C0C0", style= filled]; \n \n edge[style = invis]; \n ranksep = 0 \n nodesep = 0.1  \n bgcolor = "#EDBB99 " \n subgraph cluster_A{ \n \n label = "'+ nombrePaciente +'" \n bgcolor = "#20B2AA" \n fontcolor = white \n fontsize = 30 \n raiz[label= "", style = invis] \n edge[dir = "both"] \n '

            # variables auxiliares

            j = 1


            # creación nodos cabecera fila

            for i in range(0,filas, 1):

                graphviz += 'Fila' + str(j) +'[label = "'+ str(j) +'", group = 0]; \n' 

                j += 1

            # unimos los nodos cabecera fila

            graphviz += '\n'
            j = 1

            for i in range(0,filas-1, 1):

                graphviz += 'Fila' + str(j) + '->' + 'Fila' + str(j+1) + '; \n'

                j += 1

            # creación nodos cabecera columna

            graphviz += '\n'
            j = 1

            for i in range(0,columnas, 1):

                graphviz += 'Columna' + str(j) +'[label = "'+ str(j) +'", group = ' + str(j) + ']; \n' 

                j += 1

            # unimos los nodos cabecera columna

            graphviz += '\n'
            j = 1

            for i in range(0,columnas-1, 1):

                graphviz += 'Columna' + str(j) + '->' + 'Columna' + str(j+1) + '; \n'

                j += 1

            # unimos la raiz a la cabecera

            graphviz += '\n raiz -> Fila1 \n raiz -> Columna1 \n \n'

            # alineamos la cabecera de columna con la raiz

            graphviz += '{rank = same; raiz'
            j = 1

            for i in range(0, columnas, 1):

                graphviz += '; Columna' + str(j) 

                j += 1

            graphviz += '} \n \n'

            # Creación de nodos internos

            j = 1

            for i in range(0, filas, 1):

                inicio = self.filas.getCabeza(j)

                temp = inicio.getAcceso()

                while temp != None:

                    graphviz += 'nodo'+ str(temp.getDato().getIdCelda()) +'[label = "", fillcolor = "' +temp.getDato().getColor()+ '", group = ' +str(temp.getDato().getY())+ ']; \n'

                    temp = temp.getDerecha()

                j += 1

            # Apuntar horizontalmente todos los nodos internos con su respectiva fila

            graphviz += '\n'
            j = 1

            for i in range(0, filas, 1):

                inicio = self.filas.getCabeza(j)

                graphviz += 'Fila' + str(j) + ' -> ' + 'nodo'+ str(inicio.getAcceso().getDato().getIdCelda()) + '; \n'

                temp = inicio.getAcceso() 

                while temp.getDerecha() != None:

                    graphviz += 'nodo'+ str(temp.getDato().getIdCelda()) + ' -> ' + 'nodo' + str(temp.getDerecha().getDato().getIdCelda()) + '\n'

                    temp = temp.getDerecha()

                j += 1

            # alineamos las celdas con cada fila

            graphviz += '\n'
            j = 1

            for i in range(0, filas, 1):

                inicio = self.filas.getCabeza(j)

                graphviz += '{ rank = same; '+'Fila' + str(j)  

                temp = inicio.getAcceso() 

                while temp != None:

                    graphviz += '; nodo'+ str(temp.getDato().getIdCelda()) 

                    temp = temp.getDerecha()

                graphviz += '} \n'
                j += 1

            graphviz += '} \n } \n \n'


            documento = nombrePaciente+'.txt'
            with open(documento, 'w') as grafica:
                grafica.write(graphviz)
            pdf = nombrePaciente+'.pdf'
            os.system("dot.exe -Tpdf " + documento + " -o " + pdf )
            webbrowser.open(pdf)

