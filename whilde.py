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

# suma=0
# while True:
#     num=int(input(" ingrese numeros, cero para salir :"))
#     if num==0:
#         break
#     suma+=num
#     print(suma)
# print(f"la suma total es {suma}")

# 1 mostar par e impar
# n = int(input("Ingrese un número: "))
# if n % 2 == 0:
#     print(n, "es par.")
# else:
#     print(n, "es impar.")

# 2 mostrar la suma de todos los numeros
# total = 0
# cont=0
# opc=0
# while opc != 2:
#     print("1- agregar nuevo numero")
#     print("2- salir")
#     opc = int(input("0:"))
#     if(opc == 1):
#         num= int(input("ingrese un numero:  "))
#         cont+=1
#         total+=num
#     print(f"la cantidad de numeros ingresados son {cont}")
#     print(f"la suma de cada uno de ellos es {total}")
# 3 si el  numero es mayo a 50 logro la meta 
# from random import randint
# a = 0
# b = 0
# r = a*b
# while a*b < 50:
#     a = int(input("ingrese el valor de a: "))
#     b = randint(2,8)
#     r = a*b
#     print(f"el numero aleatorio es {b}")
#     print (f"la multiplicacion entre {a} x {b} = {r}")
#     if r < 50: 
#         print ("intente nuevamente!")
# print ("logro la meta")

# 4 ingresar num positivo y hacer operaciones basicas
num = -1
while (num < 0):
    num = int(input("ingrese un numero positivo: "))
    if (num<0):
        print("error, ingreso un numero menor a 0, vuelva a intentarlo")
print("numero ingrersado correctamente")
num = num*5     
num = num-8
num = num+3
num = num/2
print(f"el valor resultante es {num}")

# 5 adivine el numero