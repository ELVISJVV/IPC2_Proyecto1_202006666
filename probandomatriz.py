from random import randint

def llenar_matriz(n):
    matriz = []

    for r in range(n):
        fila = []

        for c in range(n):
            matriz.append(1)
        
        # matriz.append(fila)
    
    return matriz

# resultado = llenar_matriz(5)

# print(resultado)


def es_multiplo(numero, multiplo):
    # Si el residuo es 0, es múltiplo
    if numero % multiplo == 0 and numero < 10000:
        return True
    else:
        return False

print(es_multiplo(50,10))
print(es_multiplo(52,10))
print(es_multiplo(10,10))
print(es_multiplo(1,10))
print(es_multiplo(55,10))
print(es_multiplo(0,10))
print(es_multiplo(0,10))
print(es_multiplo(1500000,10))
print(es_multiplo(150,10))
