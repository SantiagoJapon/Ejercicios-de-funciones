numeros = list(input("Ingrese los valores: "))

def maximo(valores):
    mayor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor
print(maximo(numeros))