# crud de diccionarios
def MostrarJuegos(dic):
    for k, datos in dic.items:
        print(k,datos)
juegos={
    1:{"nombre": "metroid dead",
       "precio": 50000,
       "code": "ckbd231"
       },
    2: {"nombre": "pikimin 4",
        "precio": 55000,
        "code": "pKMn2022",
        }
}
MostrarJuegos(juegos)
def agregar_juegos(dic):
    ultima=list(juegos.keys())[-1]
    nombre=input("ingrese el nombre del juego: ")
    precio=int(input("ingrese el precio del juego: "))
    code=input("ingrese el codigo del juego: ")
    juegos[ultima+1]={"nombre": nombre,
            "precio":precio,
            "code":code       
            }


# MostrarJuegos(juegos)
def valida_code(clave):
    mayuscula=0
    minuscula=0
    numero=0
    for palabra in clave:
        if palabra.isupper():
            mayuscula+=1
        if palabra.islowe():
            minuscula+=1
        if palabra.isdigit():
            numero+=1
        if mayuscula==2 and minuscula==2 and numero==4: #and len(clave)==6:
            print("contraseña válida")
            return True
        else:
            print("la contraseña no es correcta, debe tener al menos una mayuscula,minuscula y numero")
            return False
def agregar_juegos(dic):
    ultima=list(dic.keys())[-1]
    nombre=input("ingrese el nombre del juego: ")
    precio=int(input("ingrese el precio del juego: "))
    while True:
        code=input("ingrese el codigo del juego: ")
        if valida_code(code):
            dic[ultima+1]={
                "nombre": nombre,
                "precio":precio,
                "code":code       
            }
            break
        else:
            print("código invalido, intente nuevamente")
def actualizar_juego(dict):
    MostrarJuegos(dict)
    act=iny(input("ingrese el nombre del juego que desea actualizar: "))
    while True:
        print('''
            1.- Nombre del juego
            2.- Precio del juego
            3.- Codigo del juego
              ''')
        dato=int(input("Que dato desea actualizar? "))
        match dato:
            case 1:
                n=input("ingrese el nuevo nombre del juego")
                dict[act]["nombre"]=n
            case 2: 
                n=input("ingrese el precio que desea actulizar: ")
                dict[act]["precio"]=n
            case 3:
                n=input("ingrese el codigo que desea actualizar ")
                if valida_code(n):
                    dict[act]["codigo"]=n
                else:
                    print("el parametro no es correcto")
                    print('''
                          el codigo debe tener, dos mayusculas, dos minusculas y cuatro numeros''')
def borrar_juego(dict):
    MostrarJuegos(dict)
    borrar=int(input("Seleccione el juego que desea borrar"))
    if borrar in dict:
        del dict[borrar]
        return True
def valida_nombre(frase):
    if " " in frase:
        return True
    else:
        return False
while True: 
        try:
            print('''
                1.- Agregar juego
                2.- Mostrar juego
                3.- Actualizar juego
                4.- Borrar juego
                5.- Salir
                ''')
            op=int(input("Seleccione una opción: "))
            match op:
                case 1:
                    agregar_juegos(juegos)
                case 2:
                    MostrarJuegos(juegos)
                case 3:
                    actualizar_juego(dict)
                case 4:
                    borrar_juego(dict)
                case _:
                    print("Opción invalida")
        except Exception:
                print("Solo numeros enteros")



