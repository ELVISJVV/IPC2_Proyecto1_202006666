class Paciente:

    def __init__(self, nombre, edad,periodos,dimension,rejillas):

        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.dimension = dimension
        self.rejillas = rejillas

    def getNombre(self):
        
        return self.nombre

    def getEdad(self):
        
        return self.edad

    def getPeriodos(self):

        return self.periodos
    
    def getDimension(self):

        return self.dimension
    
    def getRejillas(self):
        return self.rejillas


    def setNombre(self, nombre):
        
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad        

    def setPeriodos(self,periodos):
        self.periodos = periodos
    
    def setDimension(self, dimension):
        self.dimension = dimension
    
    def setRejillas(self,rejillas):
        self.rejillas = rejillas
    

    
    

