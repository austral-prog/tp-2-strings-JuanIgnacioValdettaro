def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    name=input("¿Cual es tu nombre?")
    apellido=input("¿Cual es tu apellido?")
    na= name + " " + apellido
    print(na.lower())
    print(na.title())
    print(na.upper())
    print("\t" + na.lower())

