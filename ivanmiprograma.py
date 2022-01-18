palabra_introducida = input("introduce palabra: ")
longitud = (int(len(palabra_introducida)))
# print (int (longitud))
intentos = int(input("introduce el numero de intentos: "))
lista = []
longitud_lista = (int(len(lista)))

# ADIVINAR LONGITUD LETRAS

adivinar_intentos = int(input("intenta adivinar la longitud de la palabra: "))
lista.append(adivinar_intentos)
while intentos > 1:
    intentos = intentos - 1
    if adivinar_intentos < longitud:
        print("te quedan ", intentos, "intentos")
        adivinar_intentos = int(input("la longitud es menor:"))
        lista.append(adivinar_intentos)

    if adivinar_intentos > longitud:
        print("te quedan ", intentos, "intentos")
        adivinar_intentos = int(input("la longitud es mayor: "))
        lista.append(adivinar_intentos)

    if adivinar_intentos == longitud:
        print("has acertado")
        print("tus intentos ", lista)
        break

print("intentos: ", lista)

# ELEGUIR LETRA O ADIVINAR PALABRA
elegir = int(input("elige entre 1:letra o 2:palabra ==>  "))


def letra():
    lista = []
    lista_letras_adivinadas = []
    while palabra_introducida != lista:
        letras_faltantes = 0
        lista = ""
        dime_letra = input("Adivine letra: ")
        lista_letras_adivinadas.append(dime_letra)
        for letra in palabra_introducida:
            if letra in lista_letras_adivinadas:
                lista = lista + letra
            else:
                lista = lista + "*"
                letras_faltantes = letras_faltantes + 1
        print(lista, "has acertado")
        print("te quedan por adivinar ", letras_faltantes, "letras")


def palabra():
    intentos_restantes = int(input("introduce el numero de intentos: "))
    adivina_palabra = input("dime la palabra que crees que es: ")
    while intentos_restantes > 1:

        intentos_restantes = intentos_restantes - 1

        if palabra_introducida != adivina_palabra:
            print("te quedan ", intentos_restantes, "intentos")
            adivina_palabra = input("no es correcta intentalo de nuevo ")

        else:
            print(" has acertado la palabra")
            break


if elegir == 1:
    letra()

if elegir == 2:
    palabra()
