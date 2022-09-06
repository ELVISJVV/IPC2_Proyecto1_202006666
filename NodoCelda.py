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