vocalMayuscula = ["A, E, I, O, U"]
vocalMinuscula = ["a, e, i, o, u"]

letra = None
for palabra in vocalMayuscula:
    if letra == None:
        vocalMayuscula = palabra
    else:
        if letra == None:
            vocalMinuscula = palabra

print(f'esta es una vocal mayuscula{vocalMayuscula}')
print(f'esta es una vocal minuscula{vocalMinuscula}')