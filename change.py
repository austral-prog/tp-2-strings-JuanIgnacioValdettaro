def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto=float(input())
    ingreso=int(input())
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(ingreso)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    vuelto=(ingreso-gasto)
    pesos=int(vuelto)
    print(pesos)
    print("Centavos:")
    centavos = round((vuelto - pesos) * 100)
    print(centavos)



