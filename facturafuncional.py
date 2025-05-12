datos = []

print("=======> Bienvenido, esta es su factura <=======")

def pedir_productos():
    continuar = True
    print("======> Ingrese los productos uno por uno <=====")

    while continuar:
        while True:
            producto = input(f"Producto #{len(datos) + 1}: ")
            if producto.isalnum():
                break
#Se permite el uso de letras y numeros para productos como el Vive100 o H2O
            else:
                print("No se permiten caracteres especiales")
        while True:
            precio = float(input("Ingrese el precio: "))
            if precio > 0:
                break
            else:
                print("Solo se permiten numeros positivos")
        while True:
            cantidadproducto = int(input("Cuantas unidades?: "))
#En este punto la idea es solo poner numeros enteros pero el codigo me salta error que aun no se corregir
            if cantidadproducto > 0:
                break
            else:
                print("Solo se permiten numeros positivos")
        subtotal = (cantidadproducto * precio)
        
        while True:
            validacion = input("Desea agregar mas productos? SI(Y) / NO(N) ")
            if validacion == "No" or validacion == "no" :
                continuar = False
                break
            elif validacion == "Si" or validacion == "si":
                continuar = True
                break
            else:
                print("Por favor responda Si o No")
        
        datos.append([producto,precio,cantidadproducto, "SUBTOTAL:",subtotal])

    print("\nLista de productos ingresados:")
    for idx, p in enumerate(datos, 1):
        print(f"{idx}. {p}")

        total = sum(p[4] for p in datos)
    print(f"El total de su factura es de ${total:.2f}")
        
    while True:
        descuento = float(input("Cuanto es el descuento que desea aplicar? "))
        if descuento < 0:
            print("El valor debe ser positivo")
            continuar = False
            break
        elif descuento > 100:
            print("El descuento es de 0 a 100")
            continuar = False
            break
        else:
            print(f"El total a pagar es de ${total * (1 - descuento / 100):.2f}")
#No logro crear el bucle de cuando el usuario pone un descuento que no este entre 0 a 100

        return datos
pedir_productos()