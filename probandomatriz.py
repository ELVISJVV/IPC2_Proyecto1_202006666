from random import randint

def llenar_matriz(n):
    matriz = []

    for r in range(n):
        fila = []

        for c in range(n):
            matriz.append(1)
        
        # matriz.append(fila)
    
    return matriz

resultado = llenar_matriz(5)

print(resultado)

