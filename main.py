
import xml.etree.cElementTree as ET
from ListaDoble import ListaDoble
import os
import webbrowser

if __name__ == '__main__':
    
    salir = False
    rutas = ListaDoble()
    Pacientes = ListaDoble()

    while salir == False:



        print("======= MENU PRINCIPAL ========")
        print("1. Cargar Archivo")
        print("2. Listar Pacientes")
        print("3. Seleccionar  Paciente")
        print("4. Generar Reporte")
        print("5. Salir")
        print("================================")
        opcion = input()

        if opcion == '1':
            try:
                print('Ingrese la ruta de su archivo: \n')

                ruta = input('\t -> ')

                rutas.insertar(ruta)
                print("Se han agregado los pacientes")
                print("\n")
            except:
                print("NO se pudo cargar el archivo")
                print("Intentalo Nuevamente")
                print("\n")
        
        elif opcion == '2':
            try:
                listaPacientes = rutas.cargarPacientes()
                if listaPacientes.size != 0:
                    listaPacientes.verPacientes()
                    # print("prueba")
                else:
                    print("No hay datos de pacientes")

            except:
                print("No se hallaron datos almacenados")


        elif opcion =='3':
            
            try:
                listaPacientes = rutas.cargarPacientes()
                paciente = ListaDoble()

                n = 0
                eleccion = ''

                if listaPacientes.size != 0:
                    listaPacientes.verPacientes()
                    print("Ingresa el número de paciente deseado")
                    seleccionPaciente =input()
                    # muestra paciente seleccionado 
                    nombreseleccion = listaPacientes.returnElement(int(seleccionPaciente))
                    # print(nombreseleccion)
                    paciente = listaPacientes.returnElement(int(seleccionPaciente))
                    infecciones = paciente.getDato().getCelulaInfectada()
                    mapaCuerpo = paciente.getDato().getCuerpo()
                    nombrePaciente = paciente.getDato().getNombre()
                    edadPaciente =  paciente.getDato().getEdad()
                    periodosPaciente = paciente.getDato().getPeriodos()
                    dimension = paciente.getDato().getDimension()
                    # paciente.mostrarPacientes()
                    # print(infecciones)
                    print('\n')
                    print("Nombre Paciente:  " + nombrePaciente)
                    print("Edad Paciente:  " + str(edadPaciente))
                    print("Dimension:  " + str(dimension))
                    print("Periodos:  " + str(periodosPaciente))
                    print("Rejillas Contagiadas:")
                    infecciones.mostrarRejillas()
                    # print(mapaCuerpo)
                    # print(nombrePaciente)
                    # print(dimension)
                    # print(infecciones.size)
                    # print(infecciones.returnElement(1))
                    # unidadesinfectadas = infecciones.returnElement(1)
                    # print(unidadesinfectadas.getDato().getX())
                    # print (unidadesinfectadas.getDato().getY())
                    # print(unidadesinfectadas.getDato())
                    # mapaCuerpo.mostrarMatriz()
                    # j = 1
                    # for i in range(0,infecciones.size, 1):
                                    
                    #             unidadesinfectadas = infecciones.returnElement(j)
                    #             print(unidadesinfectadas)
                    #             r=unidadesinfectadas.getDato().getX()
                    #             z=unidadesinfectadas.getDato().getY()
                    #             dato=unidadesinfectadas.getDato()
                    #             print(type(r))
                    #             print(type(z))
                    #             print("asasas")
                    #             print(type(dato))
                    #             x=int(r)
                    #             y=int(z)
                    #             mapaCuerpo.actualizarDato(x, y,dato )
                                
                    #             j += 1
                                
                    # mapaCuerpo.mostrarMatriz()
                    mapaCuerpo.graficarMapa(nombrePaciente,dimension,dimension)

                else:
                    print("No hay datos de pacientes")

            except:
                 print("No se hallaron datos almacenados")

        elif opcion == '4':


            listaPacientes = rutas.cargarPacientes()
            paciente = ListaDoble()

            
              

            if listaPacientes.size != 0:
               
                size=listaPacientes.size
            
           
                ruta=os.path.dirname(os.path.abspath(__file__))
                ruta = ruta + "/"
                # print(ruta)
                root = ET.Element("pacientes")

                i = 1
                for numero in range(1,size+1):
                    paciente = listaPacientes.returnElement(i)
                    doc = ET.SubElement(root, "paciente")
                    datosxml = ET.SubElement(doc, "datospersonales")
                    ET.SubElement(datosxml, "nombre").text=str(paciente.getDato().getNombre())
                    ET.SubElement(datosxml, "edad").text=str(paciente.getDato().getEdad())


                    ET.SubElement(doc, "periodos").text=str(paciente.getDato().getPeriodos())
                    ET.SubElement(doc, "m").text=str(paciente.getDato().getDimension())
                    ET.SubElement(doc, "resultado").text="Aún no se ha diagnosticado alguna enfermedad"

                    i += 1

                archivo = ET.ElementTree(root)
                archivo.write(ruta + "reporte.xml",xml_declaration=True,encoding="UTF-8")
                abrirArchivo=ruta+"reporte.xml"
                webbrowser.open(abrirArchivo)

            else:
                print("No hay datos de pacientes")
            
        elif opcion == '5':
            print("Hasta pronto")
            salir = True
        else:
            print("\n")
            print("Ingrese una opcion valida")
            print("\n")
    
    
    # listaPacientes.mostrarPacientes()
    