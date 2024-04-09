def suma(cadena_numero):
    if len(cadena_numero) == 0:
        return 0
    else:
        cadena_numero = cadena_numero.replace("\n", ",")
        numeros = cadena_numero.split(",")
        total = sum(int(numero) for numero in numeros)
        return total
