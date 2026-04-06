def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio=int(input())
    descuento=float(input())
    cantidad=int(input())
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    prefinal= precio-descuento
    print(f"Precio con descuento: {prefinal}")
    tot=prefinal*cantidad
    print(f"Total: {tot}")