from EPD2.Modelo.StockProducto import StockProducto
from Modelo.Electrodomestico import Electrodomestico
from Modelo.Lavadora import  Lavadora
from Modelo.Televisor import Televisor
from EPD2.GestorErrores import GestorErrores
if __name__ == "__main__":
    print("### PRUEBAS ELECTRODOMESTICO ###")
    e1 = Electrodomestico("Horno",630)
    e2 = Electrodomestico("Microondas",320)
    e3 = Electrodomestico("Lavavajillas",450)
    e4 = Electrodomestico("",-15)

    print(e1)
    print(e2)
    print(e3)
    print(e4)

    # PRUEBA ERRORES EN ELECTRODOMESTICO
    if not e4.esValido():
        print("\nErrores en e4:")
        for error in e4.getErrores():
            print(f" *{GestorErrores.getMensajeError(error)}")

    print("\n### PRUEBAS LAVADORA ###")

    lav1 = Lavadora("Balay",350,9)
    lav2 = Lavadora("Indesit",252,5)
    lav3 = Lavadora("Midea",230,6)
    lav4 = Lavadora("",-6,0)

    print(lav1)
    print(lav2)
    print(lav3)
    print(lav4)


    # PRUEBA ERRORES EN LAVADORA
    if not lav4.esValido():
        print("\nErrores en lav4:")
        for error in lav4.getErrores():
            print(f" *{GestorErrores.getMensajeError(error)}")


    print("\n### PRUEBAS TELEVISOR ###")

    tv1 = Televisor("LG",450,49.6,True)
    tv2 = Televisor("Sony",55,55.,True)
    tv3 = Televisor("Ansonic",-155,32,False)
    tv4 = Televisor("",-15,0,33)

    print(tv1)
    print(tv2)
    print(tv3)
    print(tv4)

    # PRUEBA ERRORES EN TELEVISOR
    if not tv3.esValido():
        print("\nErrores en tv3:")
        for error in tv3.getErrores():
            print(f" *{GestorErrores.getMensajeError(error)}")


    if not tv4.esValido():
        print("\nErrores en tv4:")
        for error in tv4.getErrores():
            print(f" *{GestorErrores.getMensajeError(error)}")

    print("\n### PRUEBAS STOCK ###")

    s1 = StockProducto(tv1,7)
    s2 = StockProducto(tv2,5)
    s3 = StockProducto(tv3,-2)
    s4 = StockProducto(tv4,1)

    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # PRUEBA ERRORES EN STOCK
    if not s3.esValido():
        print("\nErrores en s3:")
        for error in s3.getErrores():
            print(f" *{GestorErrores.getMensajeError(error)}")

    ## Este caso es interesante porque, a nivel de Stocl en este tv los datos no son correctos, porque no pasa las validaciones.
    # No tiene nombre, precio negativo, pulgadas cero y fullhd no es booleano
    # Sin embargo a nivel de stock si pasa las validaciones, porque stock es positivo y tiene un dato de tipo electrodomestico
    if not s4.esValido():
        print("\nErrores en s4:")
        if s4.getErrores():
            for error in s4.getErrores():
                print(f" *{GestorErrores.getMensajeError(error)}")
        else:
            print(" * El producto interno contiene errores")