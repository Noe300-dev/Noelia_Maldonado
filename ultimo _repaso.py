# repaso de listas y diccionario

# listas
#     -6 -5 -4 -3 -2 -1
# mlista=[5,7,2,9,10,2]
#       0 1 2 3 4 5
# el primero de la lista siempre va a ser 0 y el ultimo 1


# diccionario: es un conjunto de pares de datos
# dic=["mombre": "noelia Maldonado,"
#     "numero":"955361139"
#     "casada":"false"
#     "estudiante":"True"
#     "direccion":"maria elena 550"]



# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(n1+n2)

# def suma_arg(n1,n2): #funcion con argumento
#     print(n1+n2)

# def suma():
#     n1=int(input("Ingrese un numero: ")) # para que un numero tenga retorno
#     n2=int(input("Ingrese otro numero: "))
#     return (n1+n2)

# suma()
# suma_arg(9,8)
# nume=(suma_ret())
# print(nume*5)
# print(suma_ret_arg(8,9)) #tiene, retorno y argumentos

# perros de caza (ejemplo)
# perros={
#     1:{"nombre":"milo", 
#        "raza": "dog hount",
#        "código":"Dphh06"}
#     2:{"nombre":"coco", 
#        "raza": "dog hount",
#     "código":"Dphh06"}
# }
# # #                                   -1
# # perros.key() #convieete en lista [1,4]
# # #                                 0,1
# # list(perros.keys())
# def mostrar_perros(dict):
#     for key, perro in perros.items():
#          print(key, perro)
# while True:
#     try:
#         print('''
#               1.- Registrar un perro
#               2.- Mostrar perros
#               3.- Actualizar perro
#               4.- Borrar perro
#               5.- salir           
#               ''')
#         op=int(input("Seleccione una opción"))

#         match op:
#             case 1:
#                 nombre=input("ingrese un nombre")
#                 raza=input("ingrese la raza")
#                 codigo=input("ingrese su codigo alfanumérico")
#                 largo=list(perros.keys())[-1]
#                 perros[largo+1]={"nombre":nombre, 
#                             "raza": raza,
#                             "código":codigo}
#             case 2:
#                 mostrar_perros(perros)
#             case 3:
#                  mostrar_perros(perros)
#                  act=int(input("Seleccione el perro que desea actualizar"))
#                  while True:
#                     print('''
#                         1.- nombre
#                         2.- raza
#                         3.- codigo                       
#                         ''')
#                     dato=input("Que dato va a actualizar? ")
#                     match dato:
#                         case 1:
#                             n=input("ingrese el nombre ")
#                             perros[act]["nombre"]=n
#                         case 2:
#                             n=input("ingrese la nueva raza")
#                             perros[act]["raza"]=n
#                         case 3: 
#                             n=input("ingrese el nuevo codigo")
#                             perros[act]["codido"]=n
#                         case 4:
#                             break
#                         case _:
#                             print("opcion invalida")
#             case 4:
#                 mostrar_perros(perros)
#                 borrar=int(input("Seleccione el perro que desea borrar"))
#                 del perros[borrar]
#             case 4:
#                 break
#             case _:
#                 print("Opción invalida")
#     except Exception as e:
#         print("el error es: ", e)

# el codigo debe tener, una mayuscla, una minmuscula, un numero 6 caracteres

contraseña = input("Ingresa una contraseña de 6 caracteres: ")

# Verificamos el largo
if len(contraseña) != 6:
    print("La contraseña debe tener exactamente 6 caracteres.")
else:
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        print("La contraseña es válida.")
    else:
        print("La contraseña debe tener al menos una mayúscula, una minúscula y un número.")


def valida_pass(clave):
    mayuscula=False
    minuscula=False
    numero=False
    for palabra in clave:
        if palabra.isupper():
            mayuscula=True
        if palabra.islowe():
            minuscula=True
        if palabra.isdigit():
            numero=True
        if tiene_mayuscula and tiene_minuscula and tiene_numero and len(clave)==6:
            print("contraseña válida")
        else:
            print("la contraseña no es correcta, debe tener al menos una mayuscula,minuscula y numero")