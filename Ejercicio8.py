def multiplicar_lista(numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto

def suma_lista(numeros):
    producto = 0
    for numero in numeros:
        producto += numero
    return producto


numeros = [1, 2, 6, 9]
print(multiplicar_lista(numeros))
print(suma_lista(numeros))