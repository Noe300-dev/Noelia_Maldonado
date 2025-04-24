# explicacion y uso de whilde
# num=0
# while num<5:
#     print("hola")
#     num+=1

# import time


# num=10
# while num>0:
#     print(num)
#     time.sleep(1)
#     num-=1

# clave=3344
# intentos=3
# password=int(input("ingrese su clave :"))

# while clave!=password:
#     intentos-=1
#     print(f"ERROR,le quedan {intentos}, intentos")
#     password=int(input("ingrese su clave :"))
#     if intentos<=1:
#         break

# if intentos>=1:
#     print("usted ingresó al sistema")
# else:
# print("sistema logeado")

# pedir al usuario numeros que se vayan sumando
# y mostrar al final la suma de todos
# salir del programa al poner cero (0)

suma=0
while True:
    num=int(input(" ingrese numeros, cero para salir :"))
    if num==0:
        break
    suma+=num
    print(suma)
print(f"la suma total es {suma}")

    
  