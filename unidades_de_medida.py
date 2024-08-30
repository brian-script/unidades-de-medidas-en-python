print("unidades de meididas: \n")

def mm_a_cm(num):
    resultado = num / 10
    return resultado

def cm_a_mm(num):
    resultado = num * 10
    return resultado

def cm_a_m(num):
    resultado = num / 100
    return resultado

def m_a_cm(num):
    resultado = num * 100
    return resultado

def m_a_km(num):
    resultado = num / 1000
    return resultado 

def km_a_m(num):
    resultado = num * 1000
    return resultado

print("****Opciones disponibles: \n1.- mm a cm \n2.- cm a mm \n3.- cm a m \n4.- m a cm \n5.- m a km \n6.- km a m")

while True:
    try: 
        eleccion = int(input("Ingrese una de las opciones: "))
        if eleccion not in range(1, 7):
            print("\nPorfavor eliga una de las opciones mostradas en pantalla\n")
            continue



        num = int(input("Ingresa el numero que deseas convertir: "))
        break
    except:
        print("\nIngresar solo numeros\n")


if eleccion == 1:
    valor = mm_a_cm(num)
    print(f"es {valor}cm")

elif eleccion == 2:
    valor = cm_a_mm(num)
    print(f"es {valor}mm")

elif eleccion == 3:
    valor = cm_a_m(num)
    print(f"es {valor}m")

elif eleccion == 4:
    valor = m_a_cm(num)
    print(f"es {valor}cm")

elif eleccion == 5:
    valor = m_a_km(num)
    print(f"es {valor}km")

elif eleccion == 6:
    valor = km_a_m(num)
    print(f"es {valor}m")
