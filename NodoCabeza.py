class NodoCabeza:
    
    def __init__(self, id):
        
        self.id = id
        self.anterior = None
        self.siguiente = None
        self.acceso = None
    
    def getAcceso(self):
        return self.acceso

    def setAcceso(self, nuevoAcceso):
        self.acceso = nuevoAcceso