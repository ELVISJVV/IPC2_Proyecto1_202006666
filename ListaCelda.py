from Celda import Celda
import webbrowser
import os

class ListaCelda:
    
    def __init__(self):
        
        self.primero = None
        self.ultimo = None
        self.size = 0
        
    def insertarCeldaF(self, x, y, tipo):
        
        nuevo = Celda(x, y, tipo)
        
        if self.primero is None:
            
            self.primero = nuevo
            self.ultimo = nuevo
            self.size += 1
        
        else:
            
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.size += 1

    def mostrarCeldas(self):
        
        actual = self.primero
        
        while actual is not None:
            
            print('X: ' + str(actual.getX()) + ' Y: ' + str(actual.getY()) + ' Tipo: ' + actual.getTipo())
            #print()
            
            actual = actual.siguiente
        #print()
        #print()
    
    def returnCelda(self, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                return actual.getX(), actual.getY(), actual.getTipo() #solo estoy devolviendo la posición
            
            
            actual = actual.siguiente
            i += 1   

    def mostrarElementoCelda(self, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                print('X: ' + str(actual.getX()) + ' Y: ' + str(actual.getY()) + ' Tipo: ' + actual.Tipo())   #solo estoy devolviendo la posición
            
            
            actual = actual.siguiente
            i += 1   
    
    def limpiarListaCelda(self):
         
        i = 1
        
        while i < (self.size + 1):
            
            actual = self.primero.siguiente
            self.primero = None
            self.primero = actual
            
            i += 1
        
        self.size = 0  
        
    def graficarLista(self, nombrePiso, codigoPatron, r, c):
        
        Nodo = self.primero
        i = 1
        
        graphviz = 'digraph Patron{ \n node[shape =square, width = 2]; \n edge[style = invis]; \n ranksep = 0 \n nodesep = 0.1 \n subgraph Cluster_A{ \n label = "' + 'Piso:'+ nombrePiso + ' codigo: ' + codigoPatron + '"   \n fontcolor ="#FFFFFF" \n fontsize = 30 \n bgcolor ="#20B2AA" \n'
        
        #creación de nodos
        
        while Nodo is not None:
            
            if Nodo.getColor().lower() == 'W'.lower():
                
                graphviz += 'node{}[fontcolor= "#FFFFFF" fillcolor = "#FFFFFF" style = filled]; \n'.format(i)
            
            if Nodo.getColor().lower() == 'B'.lower():
                
                graphviz += 'node{}[fillcolor = "#000000" style = filled]; \n'.format(i)
            
            Nodo = Nodo.siguiente
            i += 1
            
        #union de nodos
        i = 1
        j = 2
        
        for h in range((r*c)-1):
            
            graphviz += 'node{}->node{} \n'.format(i,j)
            
            i += 1
            j += 1
        
        #Poner nodos en columna
        
        i = 1
        
        for h in range(r):
            
            
            graphviz += '{ rank = same'
            
            for g in range(c):
                
                graphviz += ';node{}'.format(i)
                i += 1
            
            graphviz += '} \n'
            
        graphviz += '} \n }'
        
        
        documento = 'grafica' + str(codigoPatron) +'.txt'
        with open(documento, 'w') as grafica:
            grafica.write(graphviz)
        pdf = 'grafica' + str(codigoPatron) +'.pdf'
        os.system("dot.exe -Tpdf " + documento + " -o " + pdf )
        webbrowser.open(pdf)    
    
    #funciones get para atributos
    def getX(self,numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                return actual.getX() 
            
            
            actual = actual.siguiente
            i += 1   
    
    def getY(self, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                return actual.getY() 
            
            
            actual = actual.siguiente
            i += 1   
    
    def getColor(self, numero):
        
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                return actual.getColor()
            
            
            actual = actual.siguiente
            i += 1   
            
    #funciones set
    def setX(self, x, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                actual.setX(x)
                
                
            actual = actual.siguiente
            i += 1   
    
    def setY(self, y, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                actual.setY(y)
                
                
            actual = actual.siguiente
            i += 1   
    
    def setColor(self, color, numero):
        
        actual = self.primero
        i = 1
        
        while actual is not None:
            
            if i == numero:
                
                actual.setColor(color)
                
                
            actual = actual.siguiente
            i += 1   