from django.http import HttpResponse


def determinarpicas(num, pos, numero):
    devuelve = 0

    for i in range(0, 4):
        if num == numero[i] and pos != (i + 1):
            devuelve = 1
            break
    return devuelve


def calcula(request, num):
    termino = False
    numero = [4, 5, 8, 1]
    contadorpicas = 0
    contadorfijas = 0

    while not termino:
        n1 = int(num / 1000)
        n2 = int((num % 1000) / 100)
        n3 = int(((num % 1000) % 100 / 10))
        n4 = int((num % 1000) % 100) % 10
        if (n1 == numero[0] and n2 == numero[1] and n3 == numero[2] and n4 ==
                numero[3]):
            respuesta = "4 fijas. Ganaste"
            return HttpResponse(respuesta)
            termino = True
        else:
            contadorpicas = contadorpicas + determinarpicas(n1, 1, numero)
            contadorpicas = contadorpicas + determinarpicas(n2, 2, numero)
            contadorpicas = contadorpicas + determinarpicas(n3, 3, numero)
            contadorpicas = contadorpicas + determinarpicas(n4, 4, numero)

            if n1 == numero[0]:
                contadorfijas = contadorfijas + 1
            if n2 == numero[1]:
                contadorfijas = contadorfijas + 1
            if n3 == numero[2]:
                contadorfijas = contadorfijas + 1
            if n4 == numero[3]:
                contadorfijas = contadorfijas + 1
            respect2 = "Usted tiene %s picas y %s fijas" % (contadorpicas,
                                                            contadorfijas)
        return HttpResponse(respect2)
