
def genFac(nombre, cantidad,productos ):
    try:
        with open("preParcial3/Facturas/" + nombre+ ".txt", "a") as fac:
                fac.write(f"""
=======================================
    Empresa: CIVILES S.A.S

    Nombre cliente: {nombre}""")
                precio_total = 0
                for i in range(len(productos)):
                    precio_total += productos[i][2]
                    fac.write(f"""

    Referencia del producto: {productos[i][0]}
    Nombre del producto: {productos[i][1]}

    Cantidad: {cantidad}
    Precio por unidad: {productos[i][2]}
    Precio total: {productos[i][3]}

    """)
                fac.write(f"Precio total: {precio_total}\n")
                fac.write("=======================================")
    except:
         with open("preParcial3/Facturas/"+nombre+".txt", "w") as fac:
                fac.write(f"""
=======================================
    Empresa: CIVILES S.A.S

    Nombre cliente: {nombre}""")
                precio_total = 0
                for i in range(len(productos)):
                    precio_total += productos[i][2]
                    fac.write(f"""

    Referencia del producto: {productos[i][0]}
    Nombre del producto: {productos[i][1]}

    Cantidad: {cantidad}
    Precio por unidad: {productos[i][2]}
    Precio total: {productos[i][3]}

    """)
                fac.write(f"Precio total: {precio_total}\n")
                fac.write("=======================================")
