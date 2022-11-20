numeros = [5,6,4,8,9,2,3,4,0,1,500,400]
menor = None
mayor = None
for numero in numeros:
    if menor == None and mayor == None:
        menor = numero
        mayor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
print(f'el numero mayor es {mayor}')
print(f'el numero menor es {menor}')