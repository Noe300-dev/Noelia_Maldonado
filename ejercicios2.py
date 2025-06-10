# lavado de autos, crear un menú para lavar autos
# 1-. cursar pago de lavado, 2-. ver ventas diarias,2-. salir
#  el lavado tiene 3 niveles
# 1-. full $12.000. 2-. standar $10.000, 3-. básico $7.000
# al mostrar las ventas diarias, debe mostrar la cantidad de autos 
# que han ingresado y el monto total 
# recaudado, también debe mostrar el monto mas alto pagado
# autos=0
# Precios=0
# # 1: 12.000
# # 2: 10.000
# # 3: 7.000
# total_autos=0
# monto_total=0
# monto_mas_alto=0

# while True: 
#     menú=int(input(''' ¿Que desea hacer?
#                    1-. Cursar el pago
#                    2-. Ver ventas diarias
#                    3-. salir
#                    '''))
#     op=int(input("seleccione una opción"))
    
#     match op:
#         case 1:
#             lavado=int(input(''' Seleccione el tipo de lavado que desea realizar (1-3)
#                              1-. Full $12.000
#                              2-. Estandar $10.000
#                              3-. Básico $7.000
#                              '''))
#             if tipo in precios:
#                 total_autos+=1
#                 monto_total+= Precios
#                 if Precios > monto_mas_alto:
#                     monto_mas_alto=Precios
#                     print(f"pago registrado por ${Precios}")
#                 else: 
#                     print("tipo de lavado invalido")
#         case 2: 
#             print("Ventas diarias")
#             print(f"total de autos lavados: {total_autos}")
#             print(f"monto total recaudado: ${monto_total}")
#             print(f"monto mas alto pagado: ${monto_mas_alto}")
#         case 3: 
#             print("Saliendo del programa...")
#             break
#         case _: 
#             print("opción invalida.")




# creación de armas Minecraft, crear espadas diamantes
# para crear una espada necesitas
# 2 diamantes y 1 palo, para obtener recursos debes tener el siguiente menú
# 1-. minar, se buscan recursos. La posibilidad de encontrar diamantes es de 1entre7 y palo
# 1 entre 3, y la de carbon es de 1 entre 3
# minar toma 3 segundos
#  2-. consultar recursos, muestra los recursos  3-. crear espadas, 4-. salir
# import random
# import time 
# d:0
# c:0
# p:0
# while True:
#     r=int(input('''
#                1. minar
#                2. consultar recursos
#                3. crear espadas
#                4. salir
#                 '''))
#     match r:
#         case 1: 
#             print("minar")
#             time.sleep(3)
#             d=random.randint(1,7)
#             d+=d
#             p=random.randint(1,3)
#             p+=p
#             c=random.randint(1,3)
#             c+=c
#         case 2: 
#             print("consultar recursos")
#             print(f"el diamante que tiene es {d}")
#             print(f"los palo que tiene son {p}")
#             print(f"el carbón que tiene es {c}")
#         case 3: 
#             print("crear espadas")
#         case 4:
#             print("salir")
