
from ListaDoble import ListaDoble


if __name__ == '__main__':
    
    salir = False
    rutas = ListaDoble()
    Pacientes = ListaDoble()

    while salir == False:



        print("======= MENU PRINCIPAL ========")
        print("1. Cargar Archivo")
        print("2. Listar Pacientes")
        print("3. Seleccionar  Paciente")
        print("4. Salir")
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
            
            # try:
                listaPacientes = rutas.cargarPacientes()
                paciente = ListaDoble()

                n = 0
                eleccion = ''

                if listaPacientes.size != 0:
                    listaPacientes.verPacientes()
                    print("Ingresa el número de paciente deseado")
                    seleccionPaciente =input()
                    # muestra paciente seleccionado 
                    # nombreseleccion = listaPacientes.returnElement(int(seleccionPaciente))
                    # print(nombreseleccion)
                    paciente = listaPacientes.returnElement(int(seleccionPaciente))
                    infecciones = paciente.getDato().getCelulaInfectada()
                    mapaCuerpo = paciente.getDato().getCuerpo()
                    nombrePaciente = paciente.getDato().getNombre()
                    dimension = paciente.getDato().getDimension()
                    print(infecciones)
                    print(mapaCuerpo)
                    print(nombrePaciente)
                    print(dimension)
                    print(infecciones.size)
                    print(infecciones.returnElement(1))
                    unidadesinfectadas = infecciones.returnElement(1)
                    print(unidadesinfectadas.getDato().getX())
                    print (unidadesinfectadas.getDato().getY())
                    print(unidadesinfectadas.getDato())
                    mapaCuerpo.mostrarMatriz()
                    j = 1
                    # for i in range(0,infecciones.size, 1):
                                    
                    #             unidadesinfectadas = infecciones.returnElement(j)
                    #             mapaCuerpo.actualizarDato(unidadesinfectadas.getDato().getX(), unidadesinfectadas.getDato().getY(), unidadesinfectadas.getDato())
                                
                    #             j += 1
                                
                    # mapaCuerpo.mostrarMatriz()
                    mapaCuerpo.graficarMapa(nombrePaciente,dimension,dimension)

                else:
                    print("No hay datos de pacientes")

            # except:
            #     print("No se hallaron datos almacenados")
            
        elif opcion == '4':
            print("Hasta pronto")
            salir = True
        else:
            print("\n")
            print("Ingrese una opcion valida")
            print("\n")
    
    
    # listaPacientes.mostrarPacientes()
    