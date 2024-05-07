from referencias import refval
from fac import genFac
def main():
    print("Bienvendo a la plataforma de compras de CIVILES S.A.S")
    nombre = input("Ingrese su nombre: ")
    print("""
          Las referencias de los productos son los siguientes:

          TZ: Teja De Zinc
          TCR: Teja Colonial Roja
          CMN: Cemento

          Q: Salir de la plataforma

          """)
    productos = []
    bandera = True
    while bandera:
        
        ref = input("Ingrese la referencia del producto: ")
        if ref.upper() == "TZ":
            cantidad = int(input("Ingrese cuantas unidades de Tejas de Zinc desea comprar: "))
            producto = refval(ref, cantidad)
            productos.append(producto)
        elif ref.upper() == "TCR":
            cantidad = float(input("Ingrese cuantos metros cuadrados de Teja Colonial Roja desea comprar: "))
            producto = refval(ref, cantidad)
            productos.append(producto)
        elif ref.upper() == "CMN":
            cantidad = int(input("Ingrese cuantas unidades de cemento desea comprar: "))
            producto = refval(ref, cantidad)
            productos.append(producto)
        elif ref.upper() == "Q":
            bandera = False
        else:
            print("Producto no encontrado")
    
    if len(productos) > 0:
        genFac(nombre, cantidad, productos)
    print("Gracias por comprar con CIVILES S.A.S")

if __name__ == "__main__":
    main()