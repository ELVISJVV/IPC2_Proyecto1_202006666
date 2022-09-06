class Paciente:

    def __init__(self,id, nombre, edad,periodos,dimension,cuerpo,celulaInfectada):
        self.id=id
        self.nombre = nombre
        self.edad = edad
        self.periodos = periodos
        self.dimension = dimension
        self.cuerpo = cuerpo
        self.celulaInfectada = celulaInfectada

    def getId(self):
        return self.id

    def getNombre(self):
        
        return self.nombre

    def getEdad(self):
        
        return self.edad

    def getPeriodos(self):

        return self.periodos
    
    def getDimension(self):

        return self.dimension
    
    def getCuerpo(self):
        return self.cuerpo

    def getCelulaInfectada(self):
        return self.celulaInfectada

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad        

    def setPeriodos(self,periodos):
        self.periodos = periodos
    
    def setDimension(self, dimension):
        self.dimension = dimension

    def setCuerpo(self, cuerpo):
        self.cuerpo = cuerpo   
    
    def setCelulaInfectada(self,celulaInfectada):
        self.celulaInfectada = celulaInfectada
    

    
    

