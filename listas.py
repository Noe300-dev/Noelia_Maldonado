# # uso y explicacion de listas
# #     -6 -5 -4 -3 -2 -1
# lista=[5,7,2,9,10,2]
# #       0 1 2 3 4 5
# print(lista[-6])# acceso al valor por indice negativo
# print(lista[0]) # acceso al valor por indice positivo
# #mostrar toda la lista
# print(lista)
# for num in lista:
#     print(num)

#hacer lista de 5 notas
#luego sacar su promedio
#las notas debem ser valores in ej: 66 70 35....
# -4 -3 -2 -1
# notas=[50,45,66,70]
# c=0
# suma=0
# # 0 1 2 4
# for nota in notas:
#     suma+=nota
#     c+=1
# prom=suma/c
# print("su promedio es ", round (prom))

# nombres=["Robin","Noelia", "Coni"]
# apellidos=["Hood", "Maldonado", "Chan"]
# print(len(nombres))
# for i in range(len(nombres)):
#     print(f"su nombre es {nombres[i]}, {apellidos[i]}")


# frutas=["sandia", "malon", "chirimoya"]
# for fruta in frutas:
#     print(f"la {frutas} tiene {len(fruta)} caracteres")

autos=["Audi", "BMW", "Toyota", "KIA", "Toyota"]
for auto in autos:
    print(auto)
    if "a" in auto.lower():
        print("La marca de auto tiene una A")
    else:
        print("No se ha encontrado marca")