

class ListaHead:
    
    def __init__(self, tipo):
        
        self.tipo = tipo
        self.primero = None
        self.ultimo = None
        self.size = 0
     
    def insertarNodoCabeza(self, nuevo):
        
        self.size += 1
        
        if self.primero ==  None:
            
            self.primero = nuevo
            self.ultimo = nuevo
        
        else:
            
            if nuevo.id < self.primero.id:
                
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo 
            
            elif nuevo.id > self.ultimo.id:
                
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
                
            else:
                
                temp = self.primero
                
                while temp != None:
                    
                    if nuevo.id < temp.id:
                        
                        nuevo.siguiente = temp
                        nuevo.anterior = temp.anterior
                        temp.anterior.siguiente = nuevo
                        temp.anterior = nuevo
                        
                        break
                        
                    elif nuevo.id > temp.id:
                        
                        temp = temp.siguiente 
                    
                    else:
                        
                        break
    
    def verListaHead(self):
        
        actual = self.primero
        
        while actual != None:
            
            print('fila: '+str(actual.id))
            actual = actual.siguiente
            
    def getCabeza(self, id):
        
        actual = self.primero
        
        while actual != None:
            
            if id == actual.id:
                
                return actual
            
            actual = actual.siguiente
        
        return None
            
    def getUltimoNodo(self):
        
        return self.ultimo.id
        
    def getPrimerNodo(self):
        
        return self.primero.id    
    
    