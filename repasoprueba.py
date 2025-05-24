# repaso de toda la unidad 2, incluye
# if, if else, elif
# while, for, match try except

# uso y manejo de except en bucle while :)
# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#         break
#     except Exception:
#         print("Solo puede ingresar numeros enteros ")
# print("su numero es ", num)

# # ejemplo de sintaxis de try
# try:
#     num=int(input("ingrese un numero: "))
# except Exception:
#         print("Solo puede ingresar numeros enteros ")
# else: #98% de las veces no se usa
#       print("si es que no hay excepción")
# finally:#99% de las veces no se usa
#       print("este bloque se ejecutara si o si, sin importar si hay excpcion o no")

# menú simple de opciones cn numeros enteros
# while True:
#     try:
#         opcion=int(input('''
#                         Seleccione una opcion con un numero entero
#                          1- opcion 1
#                          2- opcion 2
#                          3- opcion 3
#                          4- salir
#                          '''))
#         match opcion:
#              case 1:
#                 print("has seleccionado la opcion 1")
#              case 2:
#                 print("has seleccionado la opcion 2")
#              case 3:
#                 print("has seleccionado la opcion 3")
#              case 4:
#                 print("Saliendo...")
#              case _: #cualquier numero que no aparezca en case, nos envia acá
#                 print("opcion invalida")
#     except Exception:
#         print("solo puede ingresar numeros enteros")

# ejemplo de carrito cn subcategorias
# total=0
# cantart=0
# while True:
#     try:
#         opcion=int(input('''carrito de compras
#                         Seleccione una opcion con un numero entero
#                          1- comprar frutas
#                          2- comprar verduras
#                          3- pagar
#                          4- salir..
#                          '''))
#         match opcion:
#              case 1:
#                 while True:
#                         try:
#                             opcion=int(input('''
#                                             Seleccione una opcion con un numero entero
#                                             1- frutillas $1500
#                                             2- pera $1200
#                                             3- manzana $1300
#                                             4- volver al menú principal
#                                             '''))
#                             match opcion:
#                                 case 1:
#                                     print("has seleccionado frutillas")
#                                     total+=1500
#                                     cantart+=1
#                                 case 2:
#                                     print("has seleccionado pera")
#                                     total+=1200
#                                     cantart+=1
#                                 case 3:
#                                     print("has seleccionado manzana")
#                                     total+=1300
#                                     cantart+=1
#                                 case 4:
#                                     print("Saliendo...")
#                                 case _: #cualquier numero que no aparezca en case, nos envia acá
#                                     print("opcion invalida")
#                         except Exception:
#                             print("solo puede ingresar numeros enteros")
#                         print("su total hasta ahora es ", total)
#              case 2:
#                      try:
#                         opcion=int(input('''
#                             Seleccione una opcion con un numero entero
#                                                     1- papas $1500
#                                                     2- lechuga $1200
#                                                     3- zanahoria $1300
#                                                     4- volver al menú principal
#                                                     '''))
#                         match opcion:
#                                     case 1:
#                                             print("has seleccionado papas")
#                                             cant=int(input("cuantas papas llevará?"))
#                                             total+=cant*1500
#                                             cantart+=cant
#                                     case 2:
#                                             print("has seleccionado lechuga")
#                                             total+=1200
#                                             cantart+=1
#                                     case 3:
#                                         print("has seleccionado zanahorias")
#                                         total+=1300
#                                         cantart+=1
#                                     case 4:
#                                             print("Saliendo...")
#                                     case _: #cualquier numero que no aparezca en case, nos envia acá
#                                             print("opcion invalida")
#                      except Exception:
#                                      print("solo puede ingresar numeros enteros")
#                                      print("su total hasta ahora es ", total)
#              case 3:
#                 print("has seleccionado la opcion para pagar")
#                 print(f"la cantidad de articulos que lleva son {cantart}")
#                 print(f"el total a pagar es {total}")
#                 print(f"el total a pagar mas IVA es {round{total*1.19}}")
#              case 4:
#                 print("volviendo...")
#                 break
#              case _: #cualquier numero que no aparezca en case, nos envia acá
#                 print("opcion invalida")
#     except Exception:
#         print("solo puede ingresar numeros enteros")


# domingo de pascua, preguntar la cant de niños y mostrar la cant de huevos
# calificarlos asi: menos de una docena NOOB
# entre una docena a 24 MASTER
# 25 hueos o mas LEGEND
# import random
# while True:
#     try:
#         cantNiños=int(input("cuantos niños van a buscar huevitos? "))
#         while cantNiños<0
#             print("Error, ingrese numeros positivos")
#             cantNiños=int(input("cuantos niños van a buscar huevitos? "))
#         NOOB=0
#         MASTER=0
#         LEGEND=0
#         top=0 #5
#         for n in range(cantNiños):
#             cantHuevos=random.randint(5,30)
#         if cantHuevos>top: #reemplaza al numero menor :)
#             top=cantHuevos
#         print(f"el niño numero {n+1} encontro {cantHuevos} huevos") 
#         if cantHuevos<12:
#             NOOB+=1
#         elif cantHuevos>=12 and cantHuevos<=24:
#             MASTER+=1
#         else:
#             LEGEND+=1
#         print("La cantidad de NOOB es ", NOOB)
#         print("La cantidad de MASTER es ", MASTER)  
#         print("La cantidad de LEGEND es ", LEGEND)
#         print("La mayor cantidad de huevos encontrados por un niño fue ", top)
#     break
#     except Exception
# print("solo ingrese numeros enteros")

