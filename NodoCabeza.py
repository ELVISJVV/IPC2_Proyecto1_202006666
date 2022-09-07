class NodoCabeza:
    
    def __init__(self, id):
        
        self.id = id
        self.anterior = None
        self.siguiente = None
        self.__acceso = None
    
    def getAcceso(self):
        return self.__acceso

    def setAcceso(self, nuevo_acceso):
        self.__acceso = nuevo_acceso