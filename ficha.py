def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre=input()
    mail=input()
    nota1=int(input())
    nota2=int(input())
    nota3=int(input())
    titulo="""========================\n    FICHA DEL ALUMNO\n========================"""
    print(titulo)
    print(f"Nombre: {nombre.strip().title()}")
    print(f"Email: {mail.strip().lower()}")
    print(f"Caracteres en nombre: {len(nombre.strip())}")
    inicial=nombre.strip().find(" ")
    print(f"Iniciales: {nombre.strip()[0].upper()}{nombre.strip()[inicial+1:inicial+2].upper()}")
    usuario=nombre.strip()[inicial+1:] + "." + nombre.strip()[0:inicial]
    print(f"Usuario: {usuario.lower()}")
    print(f"Email valido: {'@'in mail}")
    dominio=mail.find('@')
    print(f"Dominio: {mail[dominio+1:].lower()}")
    archivo=nombre.strip().replace(' ', '_')
    print(f"Nombre para archivo: {archivo.title()}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Codigo secreto: {nombre.strip()[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    suma=nota1+nota2+nota3
    print(f"Suma: {suma}")
    promedio=(nota1+nota2+nota3)/3
    print(f"Promedio: {float(promedio)}")
    print(f"Promedio entero: {int(promedio)}")
    print("========================")



