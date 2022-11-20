menorQue = int(input("Aqui el primer numero: "))
mayorQue = int(input("Aqui el segundo numero: "))

def calculo(menorQue, mayorQue):
    if menorQue < mayorQue:
        print("Este es el numero mayor: ", menorQue)
    else:
        print("Este es el nuemero menor: ", mayorQue)
calculo(menorQue, mayorQue)