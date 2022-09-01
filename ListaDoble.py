from nodo import Nodo
from Paciente import Paciente
from Rejilla import Rejilla

#ElementTree
import xml.etree.ElementTree as ET

class ListaDoble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insertar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)
        self.size += 1 

        if self.primero == None: 

            self.primero = nuevo
            self.ultimo = nuevo
        else: 

            self.ultimo.siguiente = nuevo 
            nuevo.anterior = self.ultimo 
            self.ultimo = nuevo 
    
    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero 

        while temp != None:

            print(temp.dato) 

            temp = temp.siguiente 
    

    # Cargar los Pacientes
    def cargarPacientes(self):


        temp = self.primero

        #Lista para los pacientes
        listaPacientes = ListaDoble()

        #atributos del paciente
        nombre = ''
        edad = 0
        periodos = 0
        dimension = 0

        rejillas = ListaDoble()

        #atributos de la rejilla
        fila = ''
        columna = ''


        while temp != None:

            tree = ET.parse(temp.dato) 
            root = tree.getroot() #obtengo la etiqueta raíz

            for elemento in root: # elemento es la etiqueta <paciente>

                if elemento.tag == 'paciente':

                    for subelemento in elemento: 

                        if subelemento.tag == 'datospersonales': 

                            for sub in subelemento: # sub sera las etiquetas <nombre> <edad>

                                if sub.tag == 'nombre': 

                                    nombre = sub.text
                                    # print(nombre)
                                elif sub.tag == 'edad':

                                    edad = int(sub.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                                    # print(edad)

                        elif subelemento.tag == 'periodos': 

                            periodos = int(subelemento.text) # la propiedad "text" me devuelve un cadena con int() lo convierto a entero
                            # print(periodos)
                        elif subelemento.tag == 'm':

                            dimension = int(subelemento.text) 
                            # print(dimension)

                        elif subelemento.tag == 'rejilla': 

                            for sub in subelemento: 

                                if sub.tag == 'celda':

                                    fila = sub.get('f') 
                                    columna = sub.get('c') 
                                    # print("================")
                                    # print(fila)
                                    # print(columna)
                                    # print("==============")
                                    rejilla = Rejilla(fila, columna)
                                    rejillas.insertar(rejilla)  

                
                paciente = Paciente(nombre, edad, periodos, dimension,rejillas) 
                listaPacientes.insertar(paciente) 
                # print('++++++++++++++++++++++++++')
                #limpiar la lista rejillas
                rejillas = ListaDoble()

            temp = temp.siguiente #pasamos a la siguiente ruta un archivo xml, siempre que hayamos agregado mas.
            
        return listaPacientes 

    def mostrarPacientes(self):

        temp = self.primero 

        while temp != None:

            print('------------------------------------\nPaciente: {}\nEdad: {}\nPeriodos: {}\nDimension: {}\nRejilla:\n\n'.format(temp.dato.nombre, temp.dato.edad, temp.dato.periodos, temp.dato.dimension)) 

            temp.dato.rejillas.mostrarRejillas()

            temp = temp.siguiente 
    
    def mostrarRejillas(self):
        
        temp = self.primero 

        while temp != None:

            print('F: {}\nC: {}\n'.format(temp.dato.fila, temp.dato.columna)) 

            temp = temp.siguiente


    def obtenerPaciente(self, nombre):

        temp = self.primero

        while temp != None:

            if nombre.lower() == temp.dato.nombre.lower(): #cuando encuentre el elemento deseado retornara el dato que contiene el nodo
                return temp.dato # se retorna el dato
            
            temp = temp.siguiente #el temp recorre la lista
        
        if temp == None: #en el caso que no se haya encontrado el paciente.

            print('Paciente no encontrado.') 

    #obtener un elemento por la posición en la lista
    def obtenerElemento(self, posicion):

        i = 1 #nuestra lista comienza en la posición 1
        temp = self.primero

        while temp != None:

            if i == posicion:
                # print(temp.dato)
                return temp.dato

            i += 1
            temp = temp.siguiente
        
        if temp == None:

            print('Elemento no encontrado.')
    
    def verPacientes(self):
        
        actual = self.primero
        i = 1
        print('|------------------- Pacientes -------------------|')
        print()
        
        while actual != None:
            
            print('→ '+ str(i)+ '. ' + "Paciente: " + str(actual.getDato().getNombre()) + "   Edad: " + str(actual.getDato().getEdad()))
            print()
            
            i += 1 
            actual = actual.getSiguiente()

    def returnElement(self, posicion):
        
        actual = self.primero
        i = 1
        
        while actual != None:
            
            if posicion == i:
                
                return actual
                # return actual.dato.nombre
            
            actual = actual.getSiguiente()
            i += 1
        