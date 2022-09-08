class Celda:
    
    def __init__(self, X, Y, idCelda,color):
        
        self.coordenadaX = X
        self.coordenadaY = Y
        self.idCelda = idCelda
        self.color = color
        
        
    
    
    def getX(self):
        
        return self.coordenadaX
    
    def getY(self):
        
        return self.coordenadaY
    
    def getIdCelda(self):
        
        return self.idCelda
    
    def getColor(self):
        return self.color
    
    def setX(self, X):
        
        self.coordenadaX = X
    
    def setY(self, Y):
        
        self.coordenadaY = Y 
        
    def setIdCelda(self, idCelda):
        
        self.idCelda = idCelda

    def setColor(self, color):
        self.color = color    


class CelulaInfectada(Celda):
    def __init__(self, X, Y, idCelda,color):
    
        Celda.__init__(self, X, Y, idCelda, color)
        self.X= X
        self.Y = Y
        self.idCelda = idCelda
        self.color = color