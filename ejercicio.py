# crear un menu de carrito con las siguientes opciones
# 1- ingresar nombre del usuario
# sera mostrado en la boleta, son un saludo
# 2- comprar, poner productos para poder comprar
# con su precio correspondiente
# 3- sacar boleta mas IVA y mostrar totales
# 4- SALIR 
# consideraciones:
# por lo menos limite 3 productos
# no hay limite de compra
# se puede salir en cualquier momentos
# los montos de producto son fijos
# total=0

# nomb=int(input("Hola, ingrese su nombre por favor: "))
# while True:
#     lits=int(input('''Ingrese los productos que desea llevar
#                     1- leche $990
#                     2- pan $2000
#                     3- galletas  $1250
#                     4- salir
#                     '''))
    
#     match list:
#         case 1:
#             print("Lleva leche y su valor es ")
#             total+=900
#         case 2: 
#             print("lleva pan y su valor es " )
#             total+=2000
#         case 3: 
#             print("lleva galletas y su valor es " )
#             total+=1250
#         case 4: 
#             print("ha salido de la compra ")
#         case _:
#             print("el total neto de la compra es ", total)
#             print("el total de la compra mas IVA es ", total*1,19)

# ingrese cant de alumnos
# ingrese la nota de cada alumno
# sobre 4.0 se aprueba
# notaa=0
# cant=0
# suma=0
# a=int(input("ingrese la cantidad de alumnos"))
# for i in range(a):
#     print("Ingrese nota ", i+1)
#     nota=float(input())
#     suma+=notaa
#     prom=suma/cant
# print("El promedio es ", prom)




cantA=int(input("Ingrese el número de alumnos "))
for j in range(cantA):
    print("Ingrese el número de notas del alumno ", j+1)
    cantN=int(input())
    suma=0
    for i in range(cantN):
        print("Ingrese nota ", i+1, "del alumno ",j+1, "(use valores decimales)")
        nota=float(input())
        suma+=nota
    prom=suma/cantN
    print("El promedio es ", prom)
    if prom>=4:
        print("Usted aprobó")
    else:
        print("Usted reprobó")
