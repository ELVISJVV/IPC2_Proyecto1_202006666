class Celda:
    
    def __init__(self, x, y, idCelda,color):
        
        self.x = x
        self.y = y
        self.idCelda = idCelda
        self.color = color
        
        
    
    
    def getX(self):
        
        return self.x
    
    def getY(self):
        
        return self.y
    
    def getIdCelda(self):
        
        return self.idCelda
    
    def getColor(self):
        return self.color
    
    def setX(self, x):
        
        self.x = x   
    
    def setY(self, y):
        
        self.y = y 
        
    def setIdCelda(self, idCelda):
        
        self.idCelda = idCelda

    def setColor(self, color):
        self.color = color    