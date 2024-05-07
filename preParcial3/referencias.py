
def refval(ref, cantidad):
    ref = ref.upper()
    productos = {
        "TZ": ["Teja De Zinc", 48900, 47900, 46900, 45900],
        "TCR": ["Teja Colonial Roja", 72900, 72300, 71900, 71000],
        "CMN": ["Cemento", 20600, 19200, 18900, 18000]
    }

    # TEJA DE ZINC
    if ref == "TZ":
        if cantidad > 0 or cantidad <= 5:
            precio = productos.get(ref)[1]
        elif cantidad > 5 or cantidad <= 10:
            precio = productos.get(ref)[2]
        elif cantidad > 10 or cantidad <= 15:
            precio = productos.get(ref)[3]
        elif cantidad > 15: 
            precio = productos.get(ref)[4]

    # TEJA COLONIAL
    if ref == "TCR":
        if cantidad > 0 or cantidad <= 2.5:
            precio = productos.get(ref)[1]
        elif cantidad > 2.5 or cantidad <= 4.0:
            precio = productos.get(ref)[2]
        elif cantidad > 4.0 or cantidad <= 5.0:
            precio = productos.get(ref)[3]
        elif cantidad > 5.0: 
            precio = productos.get(ref)[4]

    # CEMENTO
    if ref == "CMN":
        if cantidad > 0 or cantidad <= 5:
            precio = productos.get(ref)[1]
        elif cantidad > 5 or cantidad <= 10:
            precio = productos.get(ref)[2]
        elif cantidad > 10 or cantidad <= 15:
            precio = productos.get(ref)[3]
        elif cantidad > 15: 
            precio = productos.get(ref)[4]
        

    return [ref, productos.get(ref)[0], precio, precio*cantidad]

