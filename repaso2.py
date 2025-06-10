# ejercicio de repaso :)
# nombre=[]
# while True:
#     print('''
#         1- insertar nombre
#         2- salir
#           ''')
#     op=int(input("seleccione una opción: "))
#     match op:
#         case 1:
#             nom=input("ingrese un nombre ")
#             nombre.append(nom)
#         case 2:
#             print("saliste...")
#             break
#         case _:
#             print("opción invalida")

# nombres=[]
# apellidos=[]
# while True:
#     print('''
#           1.- insertar nombre y apellido
#           2.- buscar nombres
#           3.- mostrar nombres
#           4.- salir
#           ''')
#     op=int(input("seleccione una opción: "))
#     match op:
#         case 1:
#             nom=input("Ingrese su nombre")
#             nombres.append(nom)
#             print(nombres)
#         case 2:
#             buscar=input("Ingrese el nombre que desea buscar")
#             if buscar in nombres:
#                 print(f"el nombre {buscar} se encuentra en la lista" )
#             else:
#                 print(f"el nombre {buscar} mo se escuentra en la lista")
#         case 3:
#             cont=0
#             for i in nombres:
#                 print(cont, "-", nombres [cont], apellidos [cont])
#         case 4:
#             print("saliendo bro")
#         case _:
#             print("opcion invalida")

# crear carrito 3.0
# tomar el carrito de comprar anterior y 
# hacerlo con listas
# 1 ingresar productos
# 2 comprar
# 3 crear boletas
# 4 salir
# que el carrito comience con 3 productos
# hay que hacer 3 listas, productos y carrito
productos=["Carne", "pollo", "jamon"]
precios=[9.000, 8790, 4500]
carritos=[]
total=0
while True:
    print('''
        1.- ingresar productos
        2.- comprar
        3.- crea boletas
        4,. salir
          ''')
    op=int(input("seleccione una opcion"))
    match op:
        case 1:
            while True:
                productos=int(input('''
                        1.- carne $9.000
                        2.- pollo $8790
                        3.- jamón $4500 
                        4.- vovler al inicio
                         '''))
                match productos:
                    case 1: 
                        nom=input("Ingrese su producto")
                        productos.append(nom)
                        apell=int(input("Ingrese un precio"))
                        precios.append(apell)
                    case 2:
                        while True:
                            for i in range(len(productos)):
                                print(i+1,"-", productos[i], "$", precios [i])
                                pro=int(input("Seleccione lo que quiere comprar"))
                                carritos.append(pro-1) #posicion en la lista
                                print(carritos)
                    case 3:
                        print("---------------0--------------")
                        print("bienvenido a carnecita muerta")
                        for i in range(len(carritos)):
                            print(productos[i], "----$", precios[i])
                            total=total+precios[i]
                            print("el total del producto es", len(carritos))
                            print("el total neto es de ", total)
                            print("su total mas IVA es de ", total*1.19)
                            print("-----0-----")
                    case 4:
                        print("Saliendo...")
                        break
                    case _:
                        print("opcion invalida")



