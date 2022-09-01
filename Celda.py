class Celda:
    
    def __init__(self, x, y, tipo):
        
        self.x = x
        self.y = y
        self.tipo = tipo
        self.siguiente = None
        
    
    
    def getX(self):
        
        return self.x
    
    def getY(self):
        
        return self.y
    
    def getTipo(self):
        
        return self.tipo
    

    
    def setX(self, x):
        
        self.x = x   
    
    def setY(self, y):
        
        self.y = y 
        
    def setTipo(self, tipo):
        
        self.tipo = tipo    