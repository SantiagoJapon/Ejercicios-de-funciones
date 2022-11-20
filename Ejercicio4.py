numeros = list(input("Ingrese los valores: "))
def minimo(valores):
    menor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] < menor:
            menor = valores[i]
        elif valores[i] == menor:
            print("Todos son iguales")
    return menor
print(minimo(numeros))